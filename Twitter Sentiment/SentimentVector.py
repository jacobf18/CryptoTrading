import pandas as pd
import pprint
from gsheets import Sheets
import requests
from textblob import TextBlob
import re
from datetime import datetime, timedelta
import time

sheets = Sheets.from_files('client_secret.json', 'storage.json')
url = 'https://docs.google.com/spreadsheets/d/1jwngP6-aeyD4hhYQJlgIBrAH0WG7vBf_oPnF5DxL9dw/edit#gid=1081976813'

s = sheets.get(url)
# Ignore the problem below.  It is not an error.
filename = 'Ethereum.csv'
s.sheets[0].to_csv(filename)

with open(filename, 'r') as fin:
    data = fin.read().splitlines(True)
with open(filename, 'w') as fout:
    fout.writelines(data[1:])

dataframe = pd.read_csv(filename)

tweets = list(dataframe['Tweet Text'])
dates = list(dataframe['Date'])

positives = 0
negatives = 0
neutrals = 0

def clean(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def strToHour(text):
    day = int(text[:text.find('/')])
    #text = text[text.find('/')+1:]
    #month = int(text[:text.find('/')])
    #text = text[text.find('/')+1:]
    #year = int(text[:text.find(' ')])
    text = text[text.find(' ')+1:]
    hour = int(text[:text.find(':')])
    return [day, hour]

sentiment = 0

sentiments = {}
accumulatedTweets = []
pastHour = 0
currentHour = 0

for i, val in enumerate(dates):
    if i == 0:
        pastHour = strToHour(val)[1]
    currentHour = strToHour(val)[1]
    if currentHour == pastHour:
        accumulatedTweets.append(tweets[i])
    else:
        sentiment = 0
        for tweet in accumulatedTweets:
            text = TextBlob(clean(tweet))
            sentiment += text.sentiment.polarity
        date = datetime.strptime(val, '%d/%m/%Y %H:%M')
        date = date.replace(minute=0)
        date = date + timedelta(hours=1)
        # Convert to UTC time
        date = date + timedelta(hours=8)
        unix = time.mktime(date.timetuple())
        key = str(int(unix*1000))
        sentiments[key] = sentiment/len(accumulatedTweets)
        accumulatedTweets = []
    if i == len(dates)-1:
        sentiment = 0
        for tweet in accumulatedTweets:
            text = TextBlob(clean(tweet))
            sentiment += text.sentiment.polarity
        date = datetime.strptime(val, '%d/%m/%Y %H:%M')
        date = date.replace(minute=0)
        # Convert to UTC time
        date = date + timedelta(hours=8)
        unix = time.mktime(date.timetuple())
        key = str(int(unix*1000))
        sentiments[key] = sentiment/len(accumulatedTweets)
    pastHour = currentHour

dataframe = pd.DataFrame.from_dict(sentiments, orient='index')
dataframe.to_csv('sentiments.csv')

