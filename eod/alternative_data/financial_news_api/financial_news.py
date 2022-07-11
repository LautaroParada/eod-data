# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:43:54 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class FinancialNews(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_FINANCIAL_NEWS = 'https://eodhistoricaldata.com/api/news'
        super().__init__(api_key, timeout)
        
    def get_financial_news(self, **query_params):
        """
        Get Financial news for a specific symbol or a specific tag. Be aware
        that the required query parameters should be s (symbol to query) or
        t (financial tag), but noth both.
        
        You can request the available tag with the get_financial_tags method

        Parameters
        ----------
        **query_params :
            query params.

        Returns
        -------
        list
            Financial news for the selected symbol or tag.

        """
        self.endpoint = self.URL_FINANCIAL_NEWS
        return super().handle_request(self.endpoint, query_params)
    
    def get_financial_tags(self):
        """
        Get the available financial news tagss

        Returns
        -------
        tags : list
            available financial tags.

        """
        tags = [
            'balance sheet', 'capital employed', 'class action', 
            'company announcement', 'consensus eps estimate', 'consensus estimate',
            'credit rating', 'discounted cash flow', 'dividend payments',
            'earnings estimate', 'earnings growth', 'earnings per share',
            'earnings release', 'earnings report', 'earnings results',
            'earnings surprise', 'estimate revisions', 'european regulatory news',
            'financial results', 'fourth quarter', 'free cash flow',
            'future cash flows', 'growth rate', 'initial public offering',
            'insider ownership', 'insider transactions', 'institutional investors',
            'institutional ownership', 'intrinsic value', 'market research reports',
            'net income', 'operating income', 'present value',
            'press releases', 'price target', 'quarterly earnings',
            'quarterly results', 'ratings', 'research analysis and reports',
            'return on equity', 'revenue estimates', 'revenue growth',
            'roce', 'roe', 'share price',
            'shareholder rights', 'shareholder', 'shares outstanding', 
            'strong buy', 'total revenue', 'zacks investment research',
            'zacks rank'
            ]
        
        return tags