from eod.alternative_data.sentiment_financial_api import SentimentFinancialData
from eod.alternative_data.financial_news_api import FinancialNews
from eod.alternative_data.macroeconomic_api import MacroEconomicIndicators

class AlternativeFinancialDataEOD(SentimentFinancialData, FinancialNews,
                                  MacroEconomicIndicators):
    def __init__(self, api_key:str, timeout:int):
        SentimentFinancialData.__init__(self, api_key, timeout)
        FinancialNews.__init__(self, api_key, timeout)
        MacroEconomicIndicators.__init__(self, api_key, timeout)