# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:13:31 2021

@author: lauta
"""

from eod.exchanges.bulk_eod_splits_divs_api import BulkMarketRequest
from eod.exchanges.list_tickers_api import ExchangesAndTickers

class ExchangesAndMarkets(BulkMarketRequest,ExchangesAndTickers):
    def __init__(self, api_key:str, timeout:int):
        BulkMarketRequest.__init__(self, api_key, timeout)
        ExchangesAndTickers.__init__(self, api_key, timeout)