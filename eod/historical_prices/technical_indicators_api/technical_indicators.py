# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:21:27 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class TechnicalIndicatorsData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL_TA = 'https://eodhistoricaldata.com/api/technical/'
        super().__init__(api_key, timeout)
        
    def get_stock_ta(self, symbol:str, **query_params):
        """
        Get the data related to the technical indicators

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params : dict
            query parameters.

        Returns
        -------
        list
            technical indicator for the selected company.

        """
        self.endpoint = self.URL_TA + symbol.upper()
        return super().handle_request(self.endpoint, query_params)