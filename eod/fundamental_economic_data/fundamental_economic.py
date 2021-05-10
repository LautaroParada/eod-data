# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:00:38 2021

@author: lauta
"""

from eod.fundamental_economic_data.fundamental_api import StockEtfFundsIndexFundamentalData

class FundamentalEconomicData(StockEtfFundsIndexFundamentalData):
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockEtfFundsIndexFundamentalData.__init__(self, api_key, timeout)