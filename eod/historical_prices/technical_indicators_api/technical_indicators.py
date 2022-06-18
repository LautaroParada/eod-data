# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:21:27 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class TechnicalIndicatorsData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        
        self.URL_TA = 'https://eodhistoricaldata.com/api/technical/'
        super().__init__(api_key, timeout)
        
        # list of available indicators
        self.ta_indicators = {
                'splitadjusted':'Split Adjusted Data',
                'avgvol':'Average Volume',
                'avgvolccy':'Average Volume by Price',
                'sma':'Simple Moving Average',
                'ema':'Exponential Moving Average',
                'wma':'Weighted Moving Average',
                'volatility':'Variance between returns',
                'stochastic':'Stochastic Technical Indicator',
                'rsi':'Relative Strength Index',
                'stddev':'Standard Deviation',
                'stochrsi':'Stochastic Relative Strength Index',
                'slope':'Linear Regression',
                'dmi':'Directional Movement Index',
                'adx':'Average Directional Movement Index',
                'macd':'Moving Average Convergence/Divergence',
                'atr':'Average True Range',
                'cci':'Commodity Channel Index',
                'sar':'Parabolic SAR',
                'bbands':'Bollinger Bands'
            }

        
    def get_instrument_ta(self, symbol:str, **query_params):
        """
        Get the data related to the technical indicators

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        list
            technical indicator for the selected company.

        """
        self.endpoint = self.URL_TA + symbol.upper()
        return super().handle_request(self.endpoint, query_params)
    
    def get_indicator_name(self):
        """
        Get the full list of the available technical indicators

        Returns
        -------
        dict
            function and name of the indicator.

        """
        return self.ta_indicators