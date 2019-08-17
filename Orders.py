import ccxt
from ccxt import OrderNotFound
from ccxt import OrderNotCached
from abc import ABC, abstractmethod

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
        print(self.exchange)
        if self.exchange.has['fetchOrder']:
            try:
                order = self.exchange.fetch_order(self.id)
                return order['status']
            except OrderNotCached:
                return 'Not Cached'
        else:
            return 'None'



class LimitBuyOrder(Order):
    def __init__(self, exchange, symbol, amount, price):
        super().__init__(exchange, symbol, amount)
        self.price = price
        self.symbol = symbol
    
    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status() + ', price: ' + str(self.price) + ']'

    def place(self):
        self.exchange.createLimitBuyOrder(self.symbol, self.amount, self.price)
        pass

        

class LimitSellOrder(Order):
    def __init__(self, exchange, symbol, amount, price):
        super().__init__(exchange, symbol, amount)
        self.price = price
        self.symbol = symbol
    
    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status() + ', price: ' + str(self.price) + ']'

    def place(self):
        self.id = self.exchange.createLimitSellOrder(self.symbol, self.amount, self.price)['id']
        pass