# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:20:59 2022

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class HistoricalMarketCapitalization(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        # base URL's of the API
        self.URL_MARKET_CAP = 'https://eodhistoricaldata.com/api/historical-market-cap/'
        super().__init__(api_key, timeout)
        
    def get_market_cap(self, symbol:str, **query_params):
        """
        Request the historical market cap (from 2017) for stocks and cryptocurrencies

        Parameters
        ----------
        symbol : str
            Financial instrument to request.
        **query_params :
            personalized parameters for the method.

        Returns
        -------
        dict
            Historical market capitalization for the specified instrument.

        """
        self.endpoint = self.URL_MARKET_CAP + symbol.upper()
        return super().handle_request(self.endpoint, query_params) 