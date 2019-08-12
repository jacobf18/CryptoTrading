import queue
from Positions import Order

class Account:
    # Initializes the Account
    # apiDict is a dictionary of exchanges and api keys
    def __init__(self, apiDict):
        self.apiDict = apiDict
        self.openOrders = queue.Queue()
        self.closeOrders = queue.Queue()
        self.closing = False

    # add an open order
    def addOpenOrder(self, order):
        if not self.closing:
            self.openOrders.put(order)
            self.submitOpenOrders()
            pass
        else:
            pass
    
    # add a close order and check 
    def addCloseOrder(self, order):
        if len(self.openOrders) > len(self.closeOrders):
            self.closeOrders.put(order)
            self.submitCloseOrders()
            pass
        else:
            pass

    # submit orders
    def submitOpenOrders(self):
        while len(self.openOrders) > 0:
            # execute order at head of queue
            self.openOrders.get().execute()
    
    def submitCloseOrders(self):
        while len(self.closeOrders) > 0:
            # execute order at head of queue
            self.closeOrders.get().execute()

    # Close any open positions and stop opening positions
    def close(self):
        self.closing = True
        
        pass

    # Hard close on the account.
    # Liquidates all positions and shuts off account.
    def liquidate(self):
        self.closing  = True

        pass

    
d = {
    'coinbase': 'askldjf',
    'poloniex': '12323123'
}
a = Account(d)