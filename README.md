# EOD Historical data SDK

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://shields.io/) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

# Contents

1. [General description](#general-description-arrow_up)
2. [Requirements](#requirements-arrow_up)
3. [Installation](#installation-arrow_up)
4. [Demo](#demo-arrow_up)
5. [Documentation](#documentation-arrow_up)
	- [Historical Prices, Splits and Dividends Data APIs](#historical-prices-splits-and-dividends-data-apis-arrow_up)
	- [Fundamental and Economic Financial Data APIs](#fundamental-and-economic-financial-data-apis-arrow_up)
	- [Exchanges Financial APIs](#exchanges-financial-apis-arrow_up)
6. [Disclaimer](#disclaimer-arrow_up)

## General description [:arrow_up:](#eod-historical-data-sdk)
This library is the Python 🐍 unofficial SDK for the EOD Historical data REST API. It's intended to be used for data extraction for financial valuations, macroeconomic analyses, sentiment analysis, option strategies, technical analysis, development of machine learning models, and more!

## Requirements [:arrow_up:](#eod-historical-data-sdk)
- You need to request an API key with the EOD team. Create your account in the following [link](https://eodhistoricaldata.com/)
	- ***Please be aware of the pricing plans and policies. Different plans have different data accesses.***
- ```Python``` >= 3.8

If any update or change is informed through the [Medium site](https://eod-historical-data.medium.com/) of the API, I will implement that in the SDK. The revisions will be on a monthly basis.

## Installation [:arrow_up:](#eod-historical-data-sdk)

```python
pip install #define a catchy name
```

## Demo [:arrow_up:](#eod-historical-data-sdk)

```python

```

## Documentation [:arrow_up:](#eod-historical-data-sdk)
Please be aware that some descriptions will come directly from the API's documentation because no further explanations were needed for the specific method. Additionally, for the sake of simplicity, I will use the following convention along with the whole document: 

```python

import # catchy library name
# create the instance of the SDK
client = EodHistoricalData(api_key)
```

### Historical Prices, Splits and Dividends Data APIs [:arrow_up:](#eod-historical-data-sdk)
- **Stock Price Data API (End-Of-Day Historical Data)**: Retrieve end-of-day data for Stocks, ETFs, Mutual Funds, Bonds (Government and Corporate), Cryptocurrencies, and FOREX pairs.
	- Parameters:
		- ```symbol```(str): Required - 
		- ```period```(str): Optional - Use 'd' for daily, 'w' for weekly, 'm' for monthly prices. By default, daily prices will be shown.
		- ```order```(str): Optional - Use 'a' for ascending dates (from old to new), 'd' for descending dates (from new to old). By default, dates are shown in ascending order.
		- ```from_```(str) and ```to```(str): Optional - The format is 'YYYY-MM-DD'. If you need data from Jan 5, 2017, to Feb 10, 2017, you should use from=2017-01-05 and to=2017-02-10.
	- Usage:
```python
# AngloAmerican stock that trades in the London Stock Exchange
resp = client.get_prices_eod('AAL.LSE', period='d', order='a', from_='2017-01-05')
# Swiss goverment Bond
resp = client.get_prices_eod('SW10Y.GBOND', period='w')
# Corportae Bond
resp = client.get_prices_eod('US00213MAS35.BOND')
```
- **Live (Delayed) Stock Prices API**: The method supports almost all symbols and exchanges worldwide, and the prices provided have a 15-20 minutes delay. The method can also provide combinations of multiple tickers with just one request. The only supported interval is the 1-minute interval. The UNIX standard is used for the timestamp.
	- Parameters:
		- ```symbol```(str): Required - Name of the instrument to retrieve data.
		- ```s```(str): Optional - Additional instruments to retrieve data.
		- ```filter_```(str): Optional - Name of the field to retrieve, check the response for the available fields.
	- Usage:
```python
# One instrument
resp = client.get_prices_live('AAL.LSE', filter_='close')
# Multple instruments
resp = client.get_prices_live('AAL.LSE', s='GLD,QVAL,QMOM,EUR.FOREX,VTI,SW10Y.GBOND')
```
- **Historical Splits, Dividends and Short Interest API**
	- Parameters:
	- Usage:
```python

```
- **Technical Indicator API**
	- Parameters:
	- Usage:
```python

```
- **Intraday Historical Data API**
	- Parameters:
	- Usage:
```python

```
- **Options Data API**
	- Parameters:
	- Usage:
```python

```
### Fundamental and Economic Financial Data APIs [:arrow_up:](#eod-historical-data-sdk)
- **Insider Transactions API**
	- Parameters:
	- Usage:
```python

```
- **Fundamental Data: Stocks, ETFs, Mutual Funds, Indices**
	- Parameters:
	- Usage:
```python

```
- **Calendar. Upcoming Earnings, Trends, IPOs and Splits**
	- Parameters:
	- Usage:
```python

```
- **Macroeconomics Data and Macro Indicators API**
	- Parameters:
	- Usage:
```python

```
- **Economic Data API**
	- Parameters:
	- Usage:
```python

```
- **Bonds Fundamentals and Historical API**
	- Parameters:
	- Usage:
```python

```
### Exchanges Financial APIs [:arrow_up:](#eod-historical-data-sdk)
- **Bulk API for EOD, Splits and Dividends**
	- Parameters:
	- Usage:
```python

```
- **Exchanges API. Get List of Tickers**
	- Parameters:
	- Usage:
```python

```
- **Exchanges API. Trading Hours and Market Holidays**
	- Parameters:
	- Usage:
```python

```
- **Financial News API**
	- Parameters:
	- Usage:
```python

```
- **Stock Market Screener API**
	- Parameters:
	- Usage:
```python

```
- **Search API for Stocks, ETFs, Mutual Funds and Indices**
	- Parameters:
	- Usage:
```python

```

## Disclaimer [:arrow_up:](#eod-historical-data-sdk)

The information in this document is for informational and educational purposes only. Nothing in this document may be construed as financial, legal or tax advice. The content of this document is solely the opinion of the author, who is not a licensed financial advisor or registered investment advisor. The author is not affiliated as a promoter of EOD Historical Data services.

This document is not an offer to buy or sell financial instruments. Never invest more than you can afford to lose. You should consult a registered professional advisor before making any investment.