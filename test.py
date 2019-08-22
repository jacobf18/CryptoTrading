# Import packages
from Account import Account
from WhaleAlert.WhaleAlert import WhaleAlert
from Orders import LimitBuyOrder, LimitSellOrder
import ccxt
import time

def printBalances():
    print('Poloniex: USDT', account.poloniex.fetch_free_balance()['USDT'])
    print('Poloniex: BTC', account.poloniex.fetch_free_balance()['BTC'])
    print('Poloniex: USDC', account.poloniex.fetch_free_balance()['USDC'])
    print('Bittrex: USDT', account.bittrex.fetch_free_balance()['USDT'])

if __name__ == '__main__':
    # Test Account functionality
    account = Account()

    # Test Orders

    #account.addOpenOrder(limitBuyOrder)
    #printBalances()

    #limitBuyOrder = LimitBuyOrder(account.poloniex, 'USDT/USDC', 2, 0.99)
    #print(limitBuyOrder.place())
    #print(limitBuyOrder.status())

    print(account.poloniex.fetch_l2_order_book('BTC/USDT'))

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality