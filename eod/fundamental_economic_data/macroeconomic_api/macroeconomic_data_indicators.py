# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:48:08 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class MacroEconomicIndicators(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_MACRO = 'https://eodhistoricaldata.com/api/macro-indicator/'
        super().__init__(api_key, timeout)
        
        #List of available macroeconomic indicators
        
    def get_macro_indicator(self, country:str, **query_params):
        """
        Get data for more than 30 macro indicators such as GDP, unemployment 
        rates, national income, price indices, inflation rates, consumption, 
        international trades, and many other significant indicators.

        Parameters
        ----------
        country : str
            Defines the country for which the indicator will be shown. The 
            country should be defined in the Alpha-3 ISO format.
        **query_params :
            query parameters.

        Returns
        -------
        list
            historical data for the selected country and indicator.

        """
        self.endpoint = self.URL_MACRO + country.upper()
        return super().handle_request(self.endpoint, query_params)