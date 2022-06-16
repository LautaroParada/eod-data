from eod.alternative_data.sentiment_financial_api import SentimentFinancialData

class AlternativeFinancialDataEOD(SentimentFinancialData):
    def __init__(self, api_key:str, timeout:int):
        SentimentFinancialData.__init__(self, api_key, timeout)