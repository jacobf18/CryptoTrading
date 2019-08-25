import time
import ccxt
from Account import Account

if __name__ == "__main__":
    account = Account()
    poloniex = account.poloniex

    print(poloniex.timeframes)
    print('BTC/USDT', poloniex.fetch_ohlcv('BTC/USDT', '1d'))
    #time.sleep (poloniex.rateLimit / 1000) # time.sleep wants seconds
    #print (symbol, poloniex.fetch_ohlcv (symbol, '1d')) # one day