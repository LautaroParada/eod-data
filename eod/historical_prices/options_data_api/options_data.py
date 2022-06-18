# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:41:50 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class StockOptionsData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_OPTIONS = 'https://eodhistoricaldata.com/api/options/'
        super().__init__(api_key, timeout)
        
    def get_stock_options(self, symbol:str, **query_params):
        """
        Stock options data for top US stocks from NYSE and NASDAQ. The options
        data is updated on a daily basis, however, the API do not provide a 
        history for options contracts prices or other data. That means: for 
        each contract, there is only the current price, bid/ask, etc.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        dict
            Stock options data for the selected company.

        """
        self.endpoint = self.URL_OPTIONS + symbol.upper()
        return super().handle_request(self.endpoint, query_params) 