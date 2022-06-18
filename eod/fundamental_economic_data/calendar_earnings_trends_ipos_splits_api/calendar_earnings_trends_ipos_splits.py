# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:14:31 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class CalendarEarningsTrendsIposSplits(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        # base URL's of the API
        self.URL_EARNINGS = 'https://eodhistoricaldata.com/api/calendar/earnings'
        self.URL_TRENDS = 'https://eodhistoricaldata.com/api/calendar/trends'
        self.URL_IPOS = 'https://eodhistoricaldata.com/api/calendar/ipos'
        self.URL_SPLITS_CALENDAR = 'https://eodhistoricaldata.com/api/calendar/splits'
        super().__init__(api_key, timeout)

    def get_calendar_earnings(self, **query_params):
        """
        Upcoming earnings for a selected stock.
        
        Parameters
        ----------
        **query_params :
            query parameters.

        Returns
        -------
        dict
            Upcoming earnings for the selected company(ies).

        """
        self.endpoint = self.URL_EARNINGS
        return super().handle_request(self.endpoint, query_params)
    
    def get_calendar_trends(self, **query_params):
        """
        Get the current trends related to earnings, growth and revenue

        Parameters
        ----------
        **query_params :
            query parameters.

        Returns
        -------
        dict
            Trends for the selected stock.

        """
        self.endpoint = self.URL_TRENDS
        return super().handle_request(self.endpoint, query_params)
    
    def get_calendar_ipos(self, **query_params):
        """
        Get the Historical and upcoming IPOs for the whole range of supported 
        exchanges.

        Parameters
        ----------
        **query_params :
            query parameters.

        Returns
        -------
        dict
            Historical and upcoming IPOs

        """
        self.endpoint = self.URL_IPOS
        return super().handle_request(self.endpoint, query_params)
    
    def get_calendar_splits(self, **query_params):
        """
        Get historical and upcoming splits for the whole range of supported 
        exchanges.

        Parameters
        ----------
        **query_params :
            query parameters.

        Returns
        -------
        dict
            Historical and upcoming splits

        """
        self.endpoint = self.URL_SPLITS_CALENDAR
        return super().handle_request(self.endpoint, query_params)