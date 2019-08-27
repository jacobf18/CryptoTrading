import pandas as pd 
import pprint

tweetSentiment = pd.read_csv('sentiments.csv')
price = pd.read_csv('poloniex-ETHUSDT-30m.csv')

c = list(price['Close'])
d = list(price['Timestamp'])

sentiments = list(tweetSentiment['Sentiment'])

closes = []
dates = []

for i, val in enumerate(c):
    if i % 2 == 0:
        closes.append(val)
        dates.append(d[i])

print(dates)

movement = []
for i, val in enumerate(closes):
    if i != len(closes)-1:
        move = closes[i+1] - val
        if move > 0:
            movement.append(1)
        else:
            movement.append(0)

vector = {}

for i, val in enumerate(sentiments):
    vector[val] = movement[i]

pp = pprint.PrettyPrinter()

pp.pprint(vector)

dataframe = pd.DataFrame.from_dict(vector, orient='index')
dataframe.to_csv('sentimentVector.csv')