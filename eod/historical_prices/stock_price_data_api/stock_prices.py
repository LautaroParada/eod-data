# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:12:30 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class StockPriceData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL_STOCK_PRICES = 'https://eodhistoricaldata.com/api/eod/'
        super().__init__(api_key, timeout)
        
    def get_prices_eod(self, symbol:str, **query_params):
        """
        Get historical prices for stocks, bonds, forex, indexes, money instruments.

        Parameters
        ----------
        symbol : str
            name of the instrument to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        list
            Historical data for the selected symbol.

        """
        self.endpoint = self.URL_STOCK_PRICES + symbol.upper()
        return super().handle_request(self.endpoint, query_params)