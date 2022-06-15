# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:22:20 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class IntradayStockData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_INTRADAY_STOCKS = 'https://eodhistoricaldata.com/api/intraday/'
        super().__init__(api_key, timeout)
        
    def get_prices_intraday(self, symbol:str, **query_params):
        """
        Get intraday historical stock price data.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        list
            intraday market data for the selected company.

        """
        self.endpoint = self.URL_INTRADAY_STOCKS + symbol.upper()
        return super().handle_request(self.endpoint, query_params) 