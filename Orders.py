import ccxt
from ccxt import OrderNotFound

class LimitBuyOrder():
    def __init__(self, exchange, symbol, amount, price):
        self.id = ''
        self.status = ''
        self.exchange = exchange
        self.amount = amount
        self.price = price
        self.symbol = symbol
    
    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status+ ']'

    def place(self):
        self.exchange.createLimitBuyOrder(self.symbol, self.amount, self.price)
        pass

    def cancel(self):
        pass

class LimitSellOrder():
    def __init__(self, exchange, symbol, amount, price):
        self.id = ''
        self.status = ''
        self.exchange = exchange
        self.amount = amount
        self.price = price
        self.symbol = symbol
    
    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status+ ']'

    def place(self):
        self.id = self.exchange.createLimitSellOrder(self.symbol, self.amount, self.price)['id']
        pass

    def cancel(self):
        try:
            self.exchange.cancel_order(self.id)
            return True
        except OrderNotFound:
            return False
        pass