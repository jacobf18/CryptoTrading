import requests
import json
import time

class WhaleAlert:
    def __init__(self, file):
        self.apikeys = []
        self.loadKeys(file)
        pass

    def receive(self, key):
        restURI = 'https://api.whale-alert.io/v1'
        now = int(time.time())
        ### Transactions
        # /transactions?api_key=your-api-key-here&min_value=500000&start=1550237797
        #print(int(now_unix - minute_ago))
        r = requests.get(restURI + '/transactions?api_key=' + key + '&start=' + str(now - 10) + '&limit=2')
        return r

    def start(self):
        while(True):
            for i in range(len(self.apikeys)):
                g = self.receive(self.apikeys[0])
                if g.json()['result'] == 'error':
                    self.apikeys.append(self.apikeys.pop(0))
                else:
                    break
        
            if 'count' in g.json() and g.json()['count'] != 0:
                print(int(time.time()), g.json())
            time.sleep(1)
    
    def loadKeys(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                line = line.replace('\n','')
                self.apikeys.append(line)