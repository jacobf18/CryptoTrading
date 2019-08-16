import ccxt

class Order:
    def __init__(self, market):
        self.id = ''
        self.status = ''
        pass

    def __str__(self):
        return 'Order[id: ' + self.id + ', status: ' + self.status+ ']'

    def place(self):
        pass

    def cancel(self):
        pass