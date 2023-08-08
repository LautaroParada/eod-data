# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:58:00 2023

@author: Shi Junjie
"""

from eod.request_handler_class import RequestHandler

class User(RequestHandler):
    
    def __init__(self, api_key:str, timeout:int):
        # base URL of the user API
        self.URL_USER = 'https://eodhistoricaldata.com/api/user/'
        super().__init__(api_key, timeout)

    def get_user(self, **query_params):
        """
        Get user details.

        Parameters
        ----------
        **query_params : TYPE
            query params.

        Returns
        -------
        list
            available exchanges to query data.

        """
        self.endpoint = self.URL_USER
        return super().handle_request(self.endpoint, query_params)
