# Import packages
from Account import Account
from WhaleAlert.WhaleAlert import WhaleAlert
from Orders import LimitOrder
import ccxt

if __name__ == '__main__':
    # Test Account functionality
    account = Account()

    # Test Orders
    order = LimitOrder(account.btcusdPoloniex, 'BTC/USD', 0.0001, 100)
    print(account.apiDict)

    #account.addOpenOrder(order)

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality