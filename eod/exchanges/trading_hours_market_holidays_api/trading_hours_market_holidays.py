# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:19:56 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class MarketHoursHolidays(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_MARKET_HOURS = 'https://eodhistoricaldata.com/api/exchange-details/'
        super().__init__(api_key, timeout)
        
    def get_exchange_details(self, exchange:str, **query_params):
        """
        Get metadata details for a specific exchange.

        Parameters
        ----------
        exchange : str
            exchange code.
        **query_params : 
            query_params.

        Returns
        -------
        dict
            metadata for the exchange.

        """
        self.endpoint = self.URL_MARKET_HOURS + exchange.upper()
        return super().handle_request(self.endpoint, query_params)