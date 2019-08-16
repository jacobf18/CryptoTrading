from Orders import LimitBuyOrder, LimitSellOrder

class ArbitragePosition:
    '''
        Exchange 1 has the overprices asset
        Exchange 2 has the underpriced asset
    '''
    def __init__(self, q, e1, e2):
        self.quantity = q
        self.exchange1 = e1
        self.exchange2 = e2
    
    def openPosition(self):
        # Buy the underpriced asset at Exchange 2
        # Short sell the overpriced asset (if margin is allowed) at Exchange 1
        pass

    def closePosition(self):
        # Sell at Exchange 2 to take profit
        # Buy back at Exchange 1 to close short position (if margin is allowed)
        pass

    def __str__(self):
        return 'Quantity: ' + str(self.quantity) + '\nExchange 1: ' + self.exchange1 + '\nExchange 2: ' + self.exchange2


def main():
    ap = ArbitragePosition(100.2, 'poloniex', 'binance')
    print(ap)

if __name__ == '__main__':
    main()