# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:00:38 2021

@author: lauta
"""

from eod.fundamental_economic_data.fundamental_api import StockEtfFundsIndexFundamentalData
from eod.fundamental_economic_data.calendar_earnings_trends_ipos_splits_api import CalendarEarningsTrendsIposSplits
from eod.fundamental_economic_data.macroeconomic_api import MacroEconomicIndicators
from eod.fundamental_economic_data.insider_transactions_api import InsiderTransactions
from eod.fundamental_economic_data.economic_events_data_api import EconomicEventsData

class FundamentalEconomicData(StockEtfFundsIndexFundamentalData, CalendarEarningsTrendsIposSplits,
                              MacroEconomicIndicators, InsiderTransactions, EconomicEventsData):
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockEtfFundsIndexFundamentalData.__init__(self, api_key, timeout)
        CalendarEarningsTrendsIposSplits.__init__(self, api_key, timeout)
        MacroEconomicIndicators.__init__(self, api_key, timeout)
        InsiderTransactions.__init__(self, api_key, timeout)
        EconomicEventsData.__init__(self, api_key, timeout)