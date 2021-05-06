# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:39:48 2021

@author: lauta
"""

import requests
import json
from typing import Dict
import logging

class RequestHandler():
    def __init__(self, api_key:str, timeout:int, endpoint:str):
        # general parameters of the api
        self.api_key = api_key
        self.timeout = timeout
        self.endpoint = endpoint
        self.resp = None
        
    # -------------------------------------------
    # Methods for data processing
    # -------------------------------------------
        
    def handle_request(self, query_params: Dict[str, str]={}):
        """
        central point to handle the requests of the API

        Parameters
        ----------
        query_params : Dict[str, str], optional
            query parameters of the request. The default is {}.

        Returns
        -------
        dict or list
            response from the API.

        """
        # append the api key and format to the parameters 
        query_params_ = self.__append_fmt(query_params)
        
        self.resp = requests.get(url=self.endpoint,
                                 params=query_params_,
                                 timeout=self.timeout)
        
        if self.resp.status_code == 200:
            return self.resp.json()
        else:
            self.resp.raise_for_status()
    
    def __append_fmt(self, dict_to_append):
        """
        Append the type of format and api key to the query parameters

        Parameters
        ----------
        dict_to_append : dict
            paramters of the request.

        Returns
        -------
        dict_to_append : dict
            full dict of paramters of the request.

        """
        dict_to_append['fmt'] = 'json'
        dict_to_append['api_token'] = self.api_key
        return dict_to_append
    
# -----------------------------------

class StockPriceData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL = 'https://eodhistoricaldata.com/api/eod/'
        self.endpoint = None
        super().__init__(api_key, timeout, '')
        
    def get_stock_prices(self, symbol:str, **query_params):
        """
        Get historical stock price data

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params : dict
            query parameters.

        Returns
        -------
        list
            Historical data for the selected symbol.

        """
        self.endpoint = self.URL + symbol.upper()
        return super().handle_request(query_params)
    
class SplitsDividendsShort(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL_DIVIDENDS = 'https://eodhistoricaldata.com/api/div/'
        self.endpoint = None
        super().__init__(api_key, timeout, '')
        
    def get_dividends(self, symbol:str, **query_params):
        """
        Get dividends for any supported ticker.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.
        
        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        self.endpoint = self.URL_DIVIDENDS + symbol.upper()
        return super().handle_request(query_params)

# -----------------------------------              

class HistoricalPrices(StockPriceData):
    
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockPriceData.__init__(self, api_key, timeout)
        SplitsDividendsShort.__init__(self, api_key, timeout)