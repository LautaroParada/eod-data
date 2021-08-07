# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:06:27 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class ExchangesAndTickers(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_EXCHANGES_LIST = 'https://eodhistoricaldata.com/api/exchanges-list/'
        self.URL_EXCH_SYMBOLS_LIST = 'https://eodhistoricaldata.com/api/exchange-symbol-list/'
        super().__init__(api_key, timeout)
        
    def get_exchanges(self, **query_params):
        """
        Get the metadata for the available exchanges.

        Parameters
        ----------
        **query_params : TYPE
            query params.

        Returns
        -------
        list
            available exchanges to query data.

        """
        self.endpoint = self.URL_EXCHANGES_LIST
        return super().handle_request(self.endpoint, query_params)
    
    def get_exchange_symbols(self, exchange:str, **query_params):
        """
        Get a list of symbols for an exchange.

        Parameters
        ----------
        exchange : str
            code for the exchange.
        **query_params : TYPE
            query params.

        Returns
        -------
        list
            available symbols for the exchange.

        """
        self.endpoint = self.URL_EXCH_SYMBOLS_LIST + exchange.upper()
        return super().handle_request(self.endpoint, query_params)