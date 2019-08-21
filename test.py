# Import packages
from Account import Account
from WhaleAlert.WhaleAlert import WhaleAlert
from Orders import LimitBuyOrder, LimitSellOrder
import ccxt
import time

if __name__ == '__main__':
    # Test Account functionality
    account = Account()

    # Test Orders

    #account.addOpenOrder(limitBuyOrder)
    print('Poloniex: USDT', account.poloniex.fetch_free_balance()['USDT'])
    print('Poloniex: BTC', account.poloniex.fetch_free_balance()['BTC'])
    print('Poloniex: USDC', account.poloniex.fetch_free_balance()['USDC'])
    print('Bittrex: USDT', account.bittrex.fetch_free_balance()['USDT'])

    #print('Poloniex: ', account.poloniex.fetch_order_book('BTC/USDT'))

    #limitBuyOrder = LimitBuyOrder(account.poloniex, 'USDT/USDC', 2, 0.99)
    #print(limitBuyOrder.place())
    #print(limitBuyOrder.status())

    # Test WhaleAlert functionality
    #w = WhaleAlert()

    # Test Positions functionality