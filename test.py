# Import packages
from Account import Account
from WhaleAlert.WhaleAlert import WhaleAlert
from Orders import LimitBuyOrder, LimitSellOrder
import ccxt

if __name__ == '__main__':
    # Test Account functionality
    account = Account()

    # Test Orders

    #account.addOpenOrder(limitBuyOrder)
    print('USDT')
    print(account.poloniex.fetch_balance()['USDT'])
    print('USDC')
    print(account.poloniex.fetch_balance()['USDC'])

    #limitBuyOrder = LimitBuyOrder(account.poloniex, 'USDT/USDC', 1, 1)
    #print(limitBuyOrder.place())

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality