# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:43:54 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class FinancialNews(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_FINANCIAL_NEWS = 'https://eodhistoricaldata.com/api/news'
        super().__init__(api_key, timeout)
        
    def get_financial_news(self, **query_params):
        """
        

        Parameters
        ----------
        **query_params : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        self.endpoint = self.URL_FINANCIAL_NEWS
        return super().handle_request(self.endpoint, query_params)