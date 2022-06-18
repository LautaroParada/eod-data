# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:28:22 2022

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class EconomicEventsData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        # base URL's of the API
        self.URL_ECONOMIC_EVENT_DATA = 'https://eodhistoricaldata.com/api/economic-events/'
        super().__init__(api_key, timeout)
        
    def get_economic_events(self, **query_params):
        """
        provides the past and future events from all around the world like 
        Retail Sails, Bond Auctions, PMI Releases and many other 
        Economic Events data.

        Parameters
        ----------
        **query_params :
            

        Returns
        -------
        dict
            Past or future ecomic events for a country.

        """
        self.endpoint = self.URL_ECONOMIC_EVENT_DATA
        return super().handle_request(self.endpoint, query_params)