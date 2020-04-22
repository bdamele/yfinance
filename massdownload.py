#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import yfinance as yf
import pandas as pd
import os

def masstickers():
    directory = 'output'
    fp = open('tickers.txt', 'r')
    fc = fp.readlines()
    fp.close()

    if not os.path.isdir(directory):
        os.mkdir(directory)

    for ticker in fc:
        ticker = ticker.strip()
        print('Retrieving data for ticker %s..' % ticker)
        try:
            tk = yf.Ticker(ticker)
            with pd.ExcelWriter(os.path.join(directory, '%s.xlsx' % ticker)) as writer:
                #pd.DataFrame(data=tk.info).to_excel(writer, sheet_name="Information")
                pd.DataFrame(data=tk.financials).to_excel(writer, sheet_name="Income statement")
                pd.DataFrame(data=tk.quarterly_financials).to_excel(writer, sheet_name="Income statement Qtr")
                pd.DataFrame(data=tk.balance_sheet).to_excel(writer, sheet_name="Balance sheet")
                pd.DataFrame(data=tk.cashflow).to_excel(writer, sheet_name="Cash flow")
                pd.DataFrame(data=tk.recommendations).to_excel(writer, sheet_name="Recommendations")
                pd.DataFrame(data=tk.sustainability).to_excel(writer, sheet_name="Sustainability")
                pd.DataFrame(data=tk.major_holders).to_excel(writer, sheet_name="Major holders")
                pd.DataFrame(data=tk.institutional_holders).to_excel(writer, sheet_name="Institutional holders")
                writer.save()
        except Exception as e:
            print("-> Failed: %s" % str(e))

if __name__ == "__main__":
    masstickers()
