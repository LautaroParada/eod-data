# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:06:37 2021

@author: lauta
"""

from eod.historical_prices import HistoricalPrices
from eod.fundamental_economic_data import FundamentalEconomicData
from eod.exchanges import ExchangesAndMarkets
from eod.alternative_data import AlternativeFinancialDataEOD

class EodHistoricalData(HistoricalPrices, FundamentalEconomicData, 
                        ExchangesAndMarkets, AlternativeFinancialDataEOD):
    def __init__(self, api_key:str, timeout:int=300):
        # Substructures of the API
        HistoricalPrices.__init__(self, api_key, timeout)
        FundamentalEconomicData.__init__(self, api_key, timeout)
        ExchangesAndMarkets.__init__(self, api_key, timeout)
        AlternativeFinancialDataEOD.__init__(self, api_key, timeout)