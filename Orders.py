import ccxt
from ccxt import OrderNotFound
from ccxt import OrderNotCached
from abc import ABC, abstractmethod

# Base class for all orders
class Order(ABC):
    def __init__(self, exchange, symbol, amount):
        self.exchange = exchange
        self.symbol = symbol
        self.amount = amount
        self.id = 'None'
        super().__init__()
    
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def place(self):
        pass

    def cancel(self):
        try:
            self.exchange.cancel_order(self.id)
            return True
        except OrderNotFound:
            return False
    
    def status(self):
        if self.exchange.has['fetchOrder']:
            try:
                order = self.exchange.fetch_order(self.id)
                return str(order['status'])
            except OrderNotCached:
                return 'Not Cached'
        else:
            return 'None'

# Limit Order to buy an asset
class LimitBuyOrder(Order):
    def __init__(self, exchange, symbol, amount, price):
        super().__init__(exchange, symbol, amount)
        self.price = price
    
    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status() + ', price: ' + str(self.price) + ', amount: ' + str(self.amount) + ']'

    def place(self):
        # Check if there is enough in the account balance to execute order
        base = self.symbol[self.symbol.find('/')+1:]
        required = self.amount * self.price
        if self.exchange.fetch_balance()[base]['free'] < required:
            print('Not enough base currency')
        else:
            # Place order on exchange
            self.id = self.exchange.createLimitBuyOrder(self.symbol, self.amount, self.price)['id']
        return self.__str__()

# Limit Order to sell an asset
class LimitSellOrder(Order):
    def __init__(self, exchange, symbol, amount, price):
        super().__init__(exchange, symbol, amount)
        self.price = price
    
    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status() + ', price: ' + str(self.price) + ', amount: ' + str(self.amount) + ']'

    def place(self):
        self.id = self.exchange.createLimitSellOrder(self.symbol, self.amount, self.price)['id']
        return self.__str__()