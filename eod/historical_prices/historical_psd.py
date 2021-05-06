# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:39:48 2021

@author: lauta
"""

from eod.historical_prices.stock_price_data_api import StockPriceData
from eod.historical_prices.hist_splits_divs_shorts_api import SplitsDividendsShort
from eod.historical_prices.live_delayed_api import LiveStockPrices

class HistoricalPrices(StockPriceData, SplitsDividendsShort, LiveStockPrices):
    
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockPriceData.__init__(self, api_key, timeout)
        SplitsDividendsShort.__init__(self, api_key, timeout)
        LiveStockPrices.__init__(self, api_key, timeout)