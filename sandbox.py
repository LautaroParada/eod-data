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
resp = client.get_live_prices(symbol, s='GLD,QVAL')
resp = client.get_dividends(symbol, from_='2020-03-01', to='2021-04-24')
resp = client.get_splits(symbol, from_='1994-01-01', to='2021-04-24')
resp = client.get_short_interest(symbol, to='2021-04-24')
resp = client.get_intraday_data(symbol, interval='1m', from_='1620136800', to='1620414000')
resp = client.get_stock_options(symbol)
resp = client.get_stock_ta(symbol, function='sma', from_='2020-03-01', to='2021-05-07', period=10)

#%% Fundamental and economic financial data

resp = client.get_fundamentals('GSPC.INDX')
# resp = client.get_bulk_fundamentals('AMEX')
resp = client.get_calendar_earnings(symbols='AAPL.US,MSFT.US,AI.PA', to='2021-12-31')
resp = client.get_calendar_trends(symbols='AAPL.US,MSFT.US,AI.PA')
resp = client.get_calendar_ipos()
resp = client.get_calendar_splits()