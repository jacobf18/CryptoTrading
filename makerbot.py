from Account import Account
from Orders import LimitBuyOrder, LimitSellOrder
import time
import ccxt

if __name__ == '__main__':
    # Create an account
    account = Account()

    # Determine the spread
    def find_maker_fee(exchange):
        return exchange.fetch_trading_fees()['maker']

    def find_profit(exchange, symbol, fee, capital):
        orderbook = exchange.fetch_l2_order_book(symbol)
        bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
        ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None
        fee = capital * 0.0015
        maxProfit = (spread * (capital/bid)) - (2 * fee) - (2 * spread / 10)
        return [bid, ask, maxProfit, len(orderbook['bids']), len(orderbook['asks']), spread]
        
    makerFee = find_maker_fee(account.poloniex)
    markets = account.poloniex.fetch_markets()
    symbols = []
    capital = 15

    for m in markets:
        base = m['symbol']
        base = base[base.find('/')+1:]
        if base == 'USDT':
            symbols.append(m['symbol'])
    
    for s in symbols:
        bid, ask, maxProfit, bidVolume, askVolume, spread = find_profit(account.poloniex, s, makerFee, capital)
        if maxProfit > 0.5:
            price = bid + (spread / 10)
            print(s, maxProfit, bid, bidVolume, askVolume, price)
            buyOrder = LimitBuyOrder(account.poloniex, s, capital / price, price)
            buyOrder.place()
            while buyOrder.status() != 'closed':
                print('Not Closed')
                time.sleep(0.01)
            print(buyOrder)
            price = ask - (spread / 10)
            sellOrder = LimitSellOrder(account.poloniex, s, capital / price, price)
            print(sellOrder)
            break