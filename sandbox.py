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
goverment_bond = 'SW10Y.GBOND'
corporate_bond = 'US00213MAS35.BOND'

#%% Historical Prices, Splits and Dividends Data API testing 

resp = client.get_stock_prices(symbol, period='d')
resp = client.get_stock_prices(goverment_bond, period='d')
resp = client.get_stock_prices(corporate_bond, period='d')
resp = client.get_live_prices(corporate_bond, s='GLD,QVAL')
resp = client.get_dividends(symbol, from_='2020-03-01', to='2021-04-24')
resp = client.get_splits(symbol, from_='1994-01-01', to='2021-04-24')
resp = client.get_short_interest(symbol, to='2021-04-24')
resp = client.get_intraday_data(symbol, interval='1m', from_='1620136800', to='1620414000')
resp = client.get_stock_options(symbol)
resp = client.get_stock_ta(symbol, function='sma', from_='2020-03-01', to='2021-05-07', period=10)

# Questions and changes

"""
1. Change the get_stock_prices to get_prices_eod -> all the supported assets can be requested with this endpoint.
2. Change get_stock_prices, get_live_prices and get_intraday_data to get_prices_something -> its the standard.
3. Does the option endpoint support options for bonds and other instruments?
4. Consider to include the full list of technical indicators as method.
5. Consider to include the filter fields -> stock prices eod and Technical indicators

"""

#%% Fundamental and economic financial data

resp = client.get_fundamentals_stock(symbol)
resp = client.get_fundamentals_bonds(cusip='US00213MAS35')
resp = client.get_calendar_earnings(symbols='AAPL.US,MSFT.US,AI.PA', to='2021-12-31')
resp = client.get_calendar_trends(symbols='AAPL.US,MSFT.US,AI.PA')
resp = client.get_calendar_ipos()
resp = client.get_calendar_splits()
resp = client.get_macro_indicator('CHL')


# Questions and changes

"""
1. Consider to include a method to list all available macro indicators

"""

#%% Exchanges API's

resp = client.get_bulk_markets(exchange='sn', filter_='extended')

# Questions and changes

"""
1. The symbols query parameter for the bulk request is not working properly.

"""