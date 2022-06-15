# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:13:08 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class LiveStockPrices(RequestHandler):
    
    def __init__(self, api_key:str, timeout:int):
        self.URL_LIVE_STOCKS = 'https://eodhistoricaldata.com/api/real-time/'
        super().__init__(api_key, timeout)
        
    def get_prices_live(self, symbol:str, **query_params):
        """
        Live (delayed) stock prices API for all subscribers of 'All-World', 
        'All World Extended', and 'ALL-IN-ONE' plans. With this API endpoint, 
        you are able to get delayed (15-20 minutes) information about almost 
        all stocks on the market.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        list
            live (delayed) stock prices of the selected companies.

        """
        self.endpoint = self.URL_LIVE_STOCKS + symbol.upper()
        return super().handle_request(self.endpoint, query_params)