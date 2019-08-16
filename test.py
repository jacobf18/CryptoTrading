# Import packages
from AccountHandling.Account import Account
from WhaleAlert.WhaleAlert import WhaleAlert
from Positions.Order import Order
import ccxt

if __name__ == '__main__':
    # Test Account functionality
    account = Account()

    # Test Orders
    order = Order(account.poloniex)

    #account.addOpenOrder(order)

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality