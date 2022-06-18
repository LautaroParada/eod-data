# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:00:38 2021

@author: lauta
"""

from eod.fundamental_economic_data.fundamental_api import StockEtfFundsIndexFundamentalData
from eod.fundamental_economic_data.calendar_earnings_trends_ipos_splits_api import CalendarEarningsTrendsIposSplits
from eod.fundamental_economic_data.insider_transactions_api import InsiderTransactions
from eod.fundamental_economic_data.historical_market_capitalization_api import HistoricalMarketCapitalization

class FundamentalEconomicData(StockEtfFundsIndexFundamentalData, CalendarEarningsTrendsIposSplits,
                              InsiderTransactions, HistoricalMarketCapitalization):
    def __init__(self, api_key:str, timeout:int):
        # inhereting the API classes
        StockEtfFundsIndexFundamentalData.__init__(self, api_key, timeout)
        CalendarEarningsTrendsIposSplits.__init__(self, api_key, timeout)
        InsiderTransactions.__init__(self, api_key, timeout)
        HistoricalMarketCapitalization.__init__(self, api_key, timeout)