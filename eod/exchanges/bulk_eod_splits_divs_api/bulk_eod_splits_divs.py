# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:14:46 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class BulkMarketRequest(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        # base URL's of the API
        self.URL_BULK_MARKET = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/'
        super().__init__(api_key, timeout)
    
    def get_bulk_markets(self, exchange:str, **query_params):
        """
        Easily download the data for the entire exchange for a particular day.
        It works for end-of-day historical data feed as well as for splits and
        dividends data. For US tickers you can also use NYSE, NASDAQ, BATS or 
        AMEX as exchange symbols to get data only for NYSE or only for NASDAQ 
        exchange.

        Parameters
        ----------
        exchange : str
            code of the exchange.
        **query_params : TYPE
            query parameters.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        self.endpoint = self.URL_BULK_MARKET + exchange.upper()
        return super().handle_request(self.endpoint, query_params)