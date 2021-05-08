# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:22:20 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class IntradayStockData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL = 'https://eodhistoricaldata.com/api/intraday/'
        super().__init__(api_key, timeout)
        
    def get_intraday_data(self, symbol:str, **query_params):
        self.endpoint = self.URL + symbol.upper()
        return super().handle_request(self.endpoint, query_params) 