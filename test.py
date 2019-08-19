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
    print('Poloniex: USDT', account.poloniex.fetch_balance()['USDT'])
    print('Poloniex: USDC', account.poloniex.fetch_balance()['USDC'])
    print('Bittrex: USDT', account.bittrex.fetch_balance()['USDT'])

    #limitBuyOrder = LimitBuyOrder(account.poloniex, 'USDT/USDC', 13, 1)
    #print(limitBuyOrder.place())

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality