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

# Stock Price Data API (End-Of-Day Historical Data)
resp = client.get_prices_eod('AAL.LSE', period='m', order='a') # stock prices - 
resp = client.get_prices_eod(goverment_bond, period='m')
resp = client.get_prices_eod(corporate_bond)
# Live (Delayed) Stock Prices API
resp = client.get_prices_live(corporate_bond, s='GLD,QVAL,QMOM,EUR.FOREX,VTI,SW10Y.GBOND,US00213MAS35.BOND') # live prices - 
# Historical Splits, Dividends and Short Interest API
resp = client.get_dividends(symbol, from_='2000-03-01', to='2021-07-06') # dividends - 
resp = client.get_splits('V.US')
# resp = client.get_short_interest(symbol, to='2021-12-31') # deleted from the client
# Intraday Historical Data API
resp = client.get_prices_intraday('EUR.FOREX', interval='5m', from_='1620136800', to='1620414000') # intraday data - check (not for bonds)
# Options Data API
resp = client.get_stock_options('AAPL') # Only for stocks - 
# Technical Indicator API
resp = client.get_indicator_name()
resp = client.get_instrument_ta('AAPL', function='bbands')


# Questions and changes

"""
DONE - 1. Change the get_stock_prices to get_prices_eod -> all the supported assets can be requested with this endpoint.
DONE - 2. Change get_stock_prices, get_live_prices and get_intraday_data to get_prices_something -> its the standard.
DONE - 3. Does the option endpoint support options for bonds and other instruments? -> NO
DONE - 4. Check the from and to parameters of the get_stock_options endpoint
DONE - 5. Consider to include the full list of technical indicators as method.
DONE - 6. Consider to include the filter fields -> stock prices eod and Technical indicators
DONE - 7. Change the name of the get_stock_ta to get_instrument_ta, all instruments have ta available.
DONE - 8. There is an issue with the SPLITS api, contact the team.
9. There is a possible error with the short interest
"""

#%% Fundamental and economic financial data

# Fundamental Data: Stocks, ETFs, Mutual Funds, Indices
resp = client.get_fundamental_equity(symbol, filter_='Financials::Balance_Sheet::quarterly') # Stock - 
resp = client.get_fundamental_equity('QVAL.US') # ETF - 
resp = client.get_fundamental_equity('SWPPX.US') # Mutual Fund - 
resp = client.get_fundamental_equity('GSPC.INDX') # Index - 
# resp = client.get_fundamentals_bulk(exchange='amex', limit=1000) # ERROR
resp = client.get_fundamentals_bonds(cusip='US00213MAS35')
# Calendar. Upcoming Earnings, Trends, IPOs and Splits
resp = client.get_calendar_earnings() # 
resp = client.get_calendar_trends(symbols='AAPL.US,MSFT.US,AI.PA') # 
resp = client.get_calendar_ipos(from_='2022-01-01') # 
resp = client.get_calendar_splits(from_='2022-01-01')
# Macroeconomics Data and Macro Indicators API
resp = client.get_macro_indicator_name()
resp = client.get_macro_indicator('CHL', indicator='real_interest_rate')
# Insider Transactions API
resp = client.get_insider_transactions(limit=100)
# Historical market capitalization
resp = client.get_market_cap(symbol='V.US', from_='2020-01-01')


# Questions and changes

"""
DONE - 1. Consider to include a method to list all available macro indicators
DONE - 2. Change the name of the method get_fundamental_stock to get_fundamental_equity
DONE - 3. Add the endpoint call related to insider transactions
DONE - 4. Check if the endpoint support the Filter Fields and WEBSERVICE support.
DONE - 5. Change the symbol to symbols parameters from the get_fundamental_bulk
6. Contact the EOD team to check the bulk fundamentals api
7. only the to parameter of the get_calendar earnings is not working

"""

#%% Exchanges API's

# Bulk API for EOD, Splits and Dividends
# additional parameters: type, date, symbols, filter
resp = client.get_bulk_markets(exchange='US', date='2022-01-01', symbols='QVAL,MSFT,QMOM,HOOD', filter_='extended')
# Exchanges API. Get List of Tickers
resp = client.get_exchanges() # Get List of Exchanges - 
resp = client.get_exchange_symbols(exchange='SN') # Get List of Tickers (Exchange Symbols) - 
# Exchanges API. Trading Hours and Market Holidays
resp = client.get_exchange_details(exchange='LSE') # 
# Search API for Stocks, ETFs, Mutual Funds and Indices
resp = client.get_search_instrument(query_string='Chile', bonds_only=1) # 
# Stock Market Screener API
resp = client.get_screener_signals()
resp = client.get_instrument_screener(signals='wallstreet_hi')


# Questions and changes

"""
DONE - 1. The symbols query parameter for the bulk request is not working properly.
DONE - 2. Why there are no news for minor international exchanges?
DONE - 3. Why the are no holidays for minor international exchanges?
4. Monitor the updates of the financial tags on a monthly basis.
PARTIALLY - 5. Try to implement the Stock Market Screener API

"""

#%% Alternative Financial Data

# Sentiment Data Financial API
resp = client.get_sentiment(s='BTC-USD.CC')
# Economic events
resp = client.get_economic_events(country='CH', comparison='mom', from_='2022-05-01')
# Financial News API
tags = client.get_financial_tags() # 
resp = client.get_financial_news(s='V.US') # choose a random tag - 
# Get the available macroindicators names
resp = client.get_macro_indicator_name()
resp = client.get_macro_indicator('CHL', indicator='population_growth_annual')
