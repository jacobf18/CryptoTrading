# Introduction
This is a framework for trading cryptocurrencies built on top of the ccxt library.  
This also includes the early stages of a Twitter Sentiment analysis bot for crypto trading.  There is a separate README for that project.

## Supported Exchanges
Poloniex  
Bittrex  
Coss  

# Setup
### Required Packages
requests  
json  
time  
ccxt  

### Api Keys
Api keys and secret keys for the exchanges must be obtained and put into a file called "ApiKeys.txt" that follows the format of the ApiKeysTemplate.txt file.

### Files not included and required
ApiKeys.txt  
WhaleAlert/WhaleAlertApiKeys.txt  

# Classes Included
## Orders
### Fields
`id` - assigned to an order once it is placed  
`exchange` - exchange an order is placed on  
`symbol` - trading pair (e.g. "BTC/USD")  
`amount` - amount of base currency (base is currency on the left, quote is on the right)  
`price` - (only for limit orders) price in quote currency to execute at
## Account
This compiles all account information into one class from multiple exchanges.  It handles the exchange classes of the ccxt libraries and closing out the account.  It also keeps track of orders.