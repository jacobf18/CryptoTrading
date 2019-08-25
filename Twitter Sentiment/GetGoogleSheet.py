import pandas as pd 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

pp = pprint.PrettyPrinter()

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Ethereum Tweets').sheet1

pp.pprint(sheet.row_values(0))

