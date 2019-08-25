# Introduction
This is an in-development project on using Twitter sentiment to predict crypto price movements.  

# Structure
Tweets are stored in a constantly updating Google Sheet that uses the Twitter Archiver Google Sheet add-on.  Sentiment for each Tweet is determined by the text-processing.com api.  
Historical crypto prices are retreived using the ccxt library.  

# To Do
Implement a machine learning model training and testing.