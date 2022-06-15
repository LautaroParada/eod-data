# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:24:15 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class StockMarketScreener(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_INSTRUMENT_SCREENER = 'https://eodhistoricaldata.com/api/screener'
        super().__init__(api_key, timeout)
        
    def get_instrument_screener(self, **query_params):
        
        self.endpoint = self.URL_INSTRUMENT_SCREENER
        return super().handle_request(self.endpoint, query_params)
    
    def get_screener_signals(self):
        available_signals = [
            '50d_new_lo, 50d_new_hi',
            '200d_new_lo, 200d_new_hi',
            'bookvalue_neg',
            'bookvalue_pos',
            'wallstreet_lo',
            'wallstreet_hi'
            ]
        
        return available_signals