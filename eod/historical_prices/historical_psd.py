# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:39:48 2021

@author: lauta
"""

from eod.historical_prices.stock_price_data_api import StockPriceData
from eod.historical_prices.splits_divs_shorts_api import SplitsDividendsShort
from eod.historical_prices.live_delayed_api import LiveStockPrices
from eod.historical_prices.intraday_hist_api import IntradayStockData
from eod.historical_prices.options_data_api import StockOptionsData
from eod.historical_prices.technical_indicators_api import TechnicalIndicatorsData

class HistoricalPrices(StockPriceData, SplitsDividendsShort, LiveStockPrices,
                       IntradayStockData, StockOptionsData, TechnicalIndicatorsData):
    
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockPriceData.__init__(self, api_key, timeout)
        SplitsDividendsShort.__init__(self, api_key, timeout)
        LiveStockPrices.__init__(self, api_key, timeout)
        IntradayStockData.__init__(self, api_key, timeout)
        StockOptionsData.__init__(self, api_key, timeout)
        #TechnicalIndicatorsData.__init__(self, api_key, timeout)