# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:39:48 2021

@author: lauta
"""

from eod.historical_prices.request_handler_class import RequestHandler
    
# -----------------------------------

class StockPriceData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL = 'https://eodhistoricaldata.com/api/eod/'
        self.endpoint = None
        super().__init__(api_key, timeout, '')
        
    def get_stock_prices(self, symbol:str, **query_params):
        """
        Get historical stock price data

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params : dict
            query parameters.

        Returns
        -------
        list
            Historical data for the selected symbol.

        """
        self.endpoint = self.URL + symbol.upper()
        return super().handle_request(query_params)
    
class SplitsDividendsShort(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL_DIVIDENDS = 'https://eodhistoricaldata.com/api/div/'
        self.endpoint = None
        super().__init__(api_key, timeout, '')
        
    def get_dividends(self, symbol:str, **query_params):
        """
        Get dividends for any supported ticker.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.
        
        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        self.endpoint = self.URL_DIVIDENDS + symbol.upper()
        return super().handle_request(query_params)

# -----------------------------------              

class HistoricalPrices(StockPriceData, SplitsDividendsShort):
    
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockPriceData.__init__(self, api_key, timeout)
        SplitsDividendsShort.__init__(self, api_key, timeout)