# -*- coding: utf-8 -*-
"""PNG_stockfilter

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p-syQIesRtF5SugatnXk82BgTNg2PUgd
"""

!pip install yfinance pandas

import yfinance as yf
import pandas as pd

stocks = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'MSFT']
wanted = ['sector', 'grossMargins', 'profitMargins', 'ebitdaMargins', 'revenueGrowth', 'enterpriseToRevenue', 'enterpriseToEbitda', 'enterpriseValue', 'priceToBook', 'beta', 'returnOnAssets', 'returnOnEquity']

def get_stock_data(stocks, wanted):
    stock_data = {}
    for stock in stocks:
        try:
            stock_info = yf.Ticker(stock).info
            stock_data[stock] = {}
            for item in wanted:
                stock_data[stock][item] = stock_info[item]
        except:
            pass
    return stock_data

def stock_filter(stock_data, gross_margin=None, ev_ebitda=None, profit_margin=None, ev_revenue=None):
    filtered_stocks = {}
    for stock, data in stock_data.items():
        if gross_margin and data['grossMargins'] < gross_margin:
            continue
        if ev_ebitda and data['enterpriseToEbitda'] > ev_ebitda:
            continue
        if profit_margin and data['profitMargins'] < profit_margin:
            continue
        if ev_revenue and data['enterpriseToRevenue'] > ev_revenue:
            continue
        filtered_stocks[stock] = data
    return filtered_stocks

stock_data = get_stock_data(stocks, wanted)
filtered_stocks = stock_filter(stock_data, gross_margin=0.15, ev_ebitda=10, profit_margin=0.05, ev_revenue=2)
for stock, data in filtered_stocks.items():
    print(f"Stock: {stock}")
    for item, value in data.items():
        print(f"{item}: {value}")
    print("\n")