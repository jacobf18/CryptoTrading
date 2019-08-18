import queue
from Orders import LimitBuyOrder, LimitSellOrder
import ccxt

class Account:
    # Initializes the Account
    # apiDict is a dictionary of exchanges and api keys
    def __init__(self):
        self.apiDict = self.loadKeys('ApiKeys.txt')
        self.openOrders = queue.Queue()
        self.closeOrders = queue.Queue()
        self.closing = False
        self.loadExchanges()
    
    def loadExchanges(self):
        ### Poloniex
        ## Does NOT have support for market orders
        # Instantiate the exchange class
        self.poloniexClass = getattr(ccxt, 'poloniex')
        self.poloniex = self.poloniexClass({
            'apiKey': self.apiDict['Poloniex'][0],
            'secret': self.apiDict['Poloniex'][1],
            'timeout': 30000,
            'enableRateLimit': True,
        })
        # Load the markets
        self.poloniex.load_markets()
        # Load the BTC/USDT market
        self.btcusdPoloniex = self.poloniex.market('BTC/USDT')

        '''
        ### Kraken
        self.krakenClass = getattr(ccxt, 'kraken')
        self.kraken = self.krakenClass({
            'apiKey': self.apiDict['Kraken'][0],
            'secret': self.apiDict['Kraken'][1],
            'timeout': 30000,
            'enableRateLimit': True,
        })
        # Load the markets
        self.kraken.load_markets()
        # Load the BTC/USDT market
        print(self.kraken.load_markets())
        self.btcusdKraken = self.kraken.market('BTC/USDT')
        

        ### Bittrex
        ## Does NOT have support for market orders
        self.bittrexClass = getattr(ccxt, 'bittrex')
        self.bittrex = self.bittrexClass({
            'apiKey': self.apiDict['Bittrex'][0],
            'secret': self.apiDict['Bittrex'][1],
            'timeout': 30000,
            'enableRateLimit': True,
        })
        # Load the markets
        self.bittrex.load_markets()
        # Load the BTC/USDT market
        self.btcusdBittrex = self.bittrex.market('BTC/USDT')

        ### COSS
        ## DOES have support for market orders
        self.cossClass = getattr(ccxt, 'coss')
        self.coss = self.cossClass({
            'apiKey': self.apiDict['Coss'][0],
            'secret': self.apiDict['Coss'][1],
            'timeout': 30000,
            'enableRateLimit': True,
        })
        # Load the markets
        self.coss.load_markets()
        # Load the BTC/USDT market
        self.btcusdCoss = self.coss.market('BTC/USDT')
        '''

    def loadKeys(self, fileName):
        apiDict = {}
        with open(fileName) as f:
            for l in f.readlines():
                key = l[:l.find(':')]
                key = key.strip()
                value = []
                apiKey = l[l.find(':')+1:l.find(',')]
                value.append(apiKey.strip())
                secretKey = l[l.find(',')+1:]
                value.append(secretKey.strip().replace('\n', ''))
                apiDict[key] = value
        return apiDict

    # add an open order
    def addOpenOrder(self, order):
        if not self.closing:
            self.openOrders.put(order)
            pass
        else:
            pass
    
    # add a close order and check 
    def addCloseOrder(self, order):
        if len(self.openOrders.queue) > len(self.closeOrders.queue):
            self.closeOrders.put(order)
            pass
        else:
            pass

    # Close any open positions and stop opening positions
    def close(self):
        self.closing = True
        pass

    # Hard close on the account.
    # Liquidates all positions and shuts off account.
    def liquidate(self):
        self.closing  = True
        pass