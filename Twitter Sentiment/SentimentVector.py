import pandas as pd
import pprint
from gsheets import Sheets

sheets = Sheets.from_files('client_secret.json', 'storage.json')
url = 'https://docs.google.com/spreadsheets/d/1jwngP6-aeyD4hhYQJlgIBrAH0WG7vBf_oPnF5DxL9dw/edit#gid=1081976813'

s = sheets.get(url)
# Ignore the problem below.  It is not an error.
s.sheets[0].to_csv('Ethereum.csv', encoding='utf-8', dialect='excel')

