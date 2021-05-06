# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:16:52 2021

@author: lauta
"""

from eod.historical_prices.request_handler_class import RequestHandler

class SplitsDividendsShort(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL_DIVIDENDS = 'https://eodhistoricaldata.com/api/div/'
        super().__init__(api_key, timeout)
        
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
        return super().handle_request(self.endpoint, query_params)