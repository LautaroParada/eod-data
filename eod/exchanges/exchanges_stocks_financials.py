# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:13:31 2021

@author: lauta
"""

from eod.exchanges.bulk_eod_splits_divs_api import BulkMarketRequest

class ExchangesAndMarkets(BulkMarketRequest):
    def __init__(self, api_key:str, timeout:int):
        BulkMarketRequest.__init__(self, api_key, timeout)