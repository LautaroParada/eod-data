# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:06:37 2021

@author: lauta
"""

from historical_prices import HistoricalPrices

class EodHistoricalData(HistoricalPrices):
    def __init__(self, api_key:str, timeout:int=300):
        # Substructures of the API
        HistoricalPrices.__init__(self, api_key, timeout)