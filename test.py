# Import packages
from Account import Account
from WhaleAlert.WhaleAlert import WhaleAlert
from Orders import LimitBuyOrder, LimitSellOrder
import ccxt

if __name__ == '__main__':
    # Test Account functionality
    account = Account()

    # Test Orders
    limitBuyOrder = LimitBuyOrder(account.poloniex, 'BTC/USD', 0.0001, 100)
    #print(account.apiDict)

    #account.addOpenOrder(limitBuyOrder)
    print(limitBuyOrder)

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality