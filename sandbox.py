# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:21:23 2021

@author: lauta
"""

import os

# load the key from the enviroment variables
api_key = os.environ['API_EOD']

from eod import EodHistoricalData

client = EodHistoricalData(api_key)
symbol='AAPL.US'

#%% Historical Prices, Splits and Dividends Data API testing 

resp = client.get_stock_prices(symbol, period='d', from_='1995-03-03', to='2021-04-24')
resp = client.get_dividends(symbol, from_='2020-03-01', to='2021-04-24')
resp = client.get_splits(symbol, from_='1994-01-01', to='2021-04-24')
resp = client.get_short_interest(symbol, to='2021-04-24')