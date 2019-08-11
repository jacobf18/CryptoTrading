import requests
import json
import time

class WhaleAlert:
    def __init__(self, file):
        # List of api keys
        self.apikeys = []
        # Loads the api keys from a file
        self.loadKeys(file)
        pass

    # Receive data from api
    def receive(self, key):
        # The start of any api call url
        restURI = 'https://api.whale-alert.io/v1'
        # The current time in UNIX time
        now = int(time.time())
        ### Transactions
        # /transactions?api_key=your-api-key-here&min_value=500000&start=1550237797
            # start	int	(Required) Unix timestamp for retrieving transactions from timestamp (exclusive). Retrieves transactions based on their execution time on the blockchain.
            # end	int	Unix timestamp for retrieving transactions until timestamp (inclusive).
            # cursor	int	Pagination key from the previous response. Recommended when retrieving transactions in intervals.
            # min_value	int	Minimum USD value of transactions returned (value at time of transaction). Allowed minimum value varies per plan ($500k for Free, $100k for Personal).
            # limit	int	Maximum number of results returned. Default 100, max 100.
            # currency	string	Returns transactions for a specific currency code. Returns all currencies by default.
        r = requests.get(restURI + '/transactions?api_key=' + key + '&start=' + str(now - 1000) + '&limit=2')
        return r

    # Start the loop of receiving data
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

    # Load the keys from a file
    def loadKeys(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                line = line.replace('\n','')
                self.apikeys.append(line)
