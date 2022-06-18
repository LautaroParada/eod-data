# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:48:08 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class MacroEconomicIndicators(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_MACRO = 'https://eodhistoricaldata.com/api/macro-indicator/'
        super().__init__(api_key, timeout)
        
        #List of available macroeconomic indicators
        self.macro_indicators = {
            'real_interest_rate':'Real interest rate (%)',
            'population_total':'Population, total',
            'population_growth_annual':'Population growth (annual %)',
            'inflation_consumer_prices_annual':'Inflation, consumer prices (annual %)',
            'gdp_current_usd':'GDP (current US$)',
            'gdp_per_capita_usd':'GDP per capita (current US$)',
            'gdp_growth_annual':'GDP growth (annual %)',
            'debt_percent_gdp':'Debt in percent of GDP (annual %)',
            'net_trades_goods_services':'Net trades in goods and services (current US$)',
            'inflation_gdp_deflator_annual':'Inflation, GDP deflator (annual %)',
            'agriculture_value_added_percent_gdp':'Agriculture, value added (% of GDP)',
            'industry_value_added_percent_gdp':'Industry, value added (% of GDP)',
            'services_value_added_percent_gdp':'Services, etc,, value added (% of GDP)',
            'exports_of_goods_services_percent_gdp':'Exports of goods and services (% of GDP)',
            'imports_of_goods_services_percent_gdp':'Imports of goods and services (% of GDP)',
            'gross_capital_formation_percent_gdp':'Gross capital formation (% of GDP)',
            'net_migration':'Net migration (absolute value)',
            'gni_usd':'GNI, Atlas method (current US$)',
            'gni_per_capita_usd':'GNI per capita, Atlas method (current US$)',
            'gni_ppp_usd':'GNI, PPP (current international $)',
            'gni_per_capita_ppp_usd':'GNI per capita, PPP (current international $)',
            'income_share_lowest_twenty':'Income share held by lowest 20% (in %)',
            'life_expectancy':'Life expectancy at birth, total (years)',
            'fertility_rate':'Fertility rate, total (births per woman)',
            'prevalence_hiv_total':'Prevalence of HIV, total (% of population ages 15-49)',
            'co2_emissions_tons_per_capita':'CO2 emissions (metric tons per capita)',
            'surface_area_km':'Surface area (sq, km)',
            'poverty_poverty_lines_percent_population':'Poverty headcount ratio at national poverty lines (% of population)',
            'revenue_excluding_grants_percent_gdp':'Revenue, excluding grants (% of GDP)',
            'cash_surplus_deficit_percent_gdp':'Cash surplus/deficit (% of GDP)',
            'startup_procedures_register':'Start-up procedures to register a business (number)',
            'market_cap_domestic_companies_percent_gdp':'Market capitalization of listed domestic companies (% of GDP)',
            'mobile_subscriptions_per_hundred':'Mobile cellular subscriptions (per 100 people)',
            'internet_users_per_hundred':'Internet users (per 100 people)',
            'high_technology_exports_percent_total':'High-technology exports (% of manufactured exports)',
            'merchandise_trade_percent_gdp':'Merchandise trade (% of GDP)',
            'total_debt_service_percent_gni':'Total debt service (% of GNI)'
            }
        
    def get_macro_indicator(self, country:str, **query_params):
        """
        Get data for more than 30 macro indicators such as GDP, unemployment 
        rates, national income, price indices, inflation rates, consumption, 
        international trades, and many other significant indicators.

        Parameters
        ----------
        country : str
            Defines the country for which the indicator will be shown. The 
            country should be defined in the Alpha-3 ISO format.
        **query_params :
            query parameters.

        Returns
        -------
        list
            historical data for the selected country and indicator.

        """
        self.endpoint = self.URL_MACRO + country.upper()
        return super().handle_request(self.endpoint, query_params)
    
    def get_macro_indicator_name(self):
        return self.macro_indicators