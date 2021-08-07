# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:21:23 2021

@author: lauta
"""

import os

# load the key from the enviroment variables
api_key = os.environ['API_EOD']

from eod import EodHistoricalData
from random import randint

client = EodHistoricalData(api_key)
symbol='AAPL.US'
goverment_bond = 'SW10Y.GBOND'
corporate_bond = 'US00213MAS35.BOND'

#%% Historical Prices, Splits and Dividends Data API testing 

# Stock Price Data API (End-Of-Day Historical Data)
resp = client.get_stock_prices('AAL.LSE', period='m', order='a') # stock prices - check
resp = client.get_stock_prices(goverment_bond, period='d')
resp = client.get_stock_prices(corporate_bond, period='d')
# Live (Delayed) Stock Prices API
resp = client.get_live_prices(corporate_bond, s='GLD,QVAL,QMOM,EUR.FOREX,VTI,SW10Y.GBOND,US00213MAS35.BOND') # live prices - check
# Historical Splits, Dividends and Short Interest API
resp = client.get_dividends(symbol, from_='2000-03-01', to='2021-07-06') # dividends - check
resp = client.get_splits(symbol, from_='1994-01-01', to='2021-07-04') # ERROR
resp = client.get_short_interest(symbol, to='2021-07-04')
# Intraday Historical Data API
resp = client.get_intraday_data('EUR.FOREX', interval='5m', from_='1620136800', to='1620414000') # intraday data - check (not for bonds)
# Options Data API
resp = client.get_stock_options('AAPL') # Only for stocks - check
# Technical Indicator API
resp = client.get_stock_ta('EUR.FOREX', function='sma', from_='2020-03-01', to='2021-06-30', period=50, filter_='last_ema')


# Questions and changes

"""
1. Change the get_stock_prices to get_prices_eod -> all the supported assets can be requested with this endpoint.
2. Change get_stock_prices, get_live_prices and get_intraday_data to get_prices_something -> its the standard.
3. Does the option endpoint support options for bonds and other instruments? -> NO
4. Check the from and to parameters of the get_stock_options endpoint
5. Consider to include the full list of technical indicators as method.
6. Consider to include the filter fields -> stock prices eod and Technical indicators
7. Change the name of the get_stock_ta to get_instrument_ta, all instruments have ta available.

"""

#%% Fundamental and economic financial data

resp = client.get_fundamentals_stock(symbol)
resp = client.get_fundamentals_bonds(cusip='US00213MAS35')
resp = client.get_calendar_earnings(symbols='AAPL.US,MSFT.US,AI.PA', to='2021-06-30')
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
resp = client.get_exchanges()
resp = client.get_exchange_symbols('IS')
resp = client.get_exchange_details(exchange='LSE', from_='2020-12-20', to='2021-05-18')
tags = client.get_financial_tags()
resp = client.get_financial_news(t=tags[randint(a=0, b=len(tags))]) # choose a random tag
resp = client.get_search_instrument(query_string='Latam', bonds_only=1)


# Questions and changes

"""
1. The symbols query parameter for the bulk request is not working properly.
2. Why there are no news for minor international exchanges?
3. Why the are no holidays for minor international exchanges?

"""