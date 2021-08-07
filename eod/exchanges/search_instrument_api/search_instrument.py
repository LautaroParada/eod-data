# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:37:42 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class SearchInstrument(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_SEARCH_INSTRUMENT = 'https://eodhistoricaldata.com/api/search/'
        super().__init__(api_key, timeout)
        
    def get_search_instrument(self, query_string:str, **query_params):
        """
        Search Bonds, ETFs, Mutual Funds, Companies, etc by ISIN or a word.

        Parameters
        ----------
        query_string : str
            Asset name or code or even ISIN.
        **query_params :
            query params.

        Returns
        -------
        list
            results for the search.

        """
        self.endpoint = self.URL_SEARCH_INSTRUMENT + query_string
        return super().handle_request(self.endpoint, query_params)