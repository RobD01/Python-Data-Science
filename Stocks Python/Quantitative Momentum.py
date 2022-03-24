# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:01:37 2022

@author: medbz
"""

import numpy as np
import pandas as pd
import requests
import math
from scipy import stats

import xlsxwriter

#API token and stocks list
stocks = pd.read_csv (r'sp_500_stocks.csv')
from secrets import IEX_CLOUD_API_TOKEN

# =============================================================================
# #API Call
# symbol = 'AAPL'
# api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/stats/?token={IEX_CLOUD_API_TOKEN}' 
# 
# data = requests.get(api_url).json()
# 
# print(data['year1ChangePercent'])
# =============================================================================

# setting up data frame and stock list
print("Creating Data Table... ")
stocks = pd.read_csv (r'sp_500_stocks.csv')

# Advanced Momentum
hqm_columns = [
        'Ticker', 
        'Stock Price', 
        'Number of Shares',
        '1 Year Return',
        '6 Month Return',
        '3 Month Return',
        '1 Month Return',
        ]

hqm_dataframe = pd.DataFrame(columns = hqm_columns)

#batch API request in free version limited to chunks of #100
print("Accessing API Data... ")
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

        
symbol_groups = list( chunks( stocks['Ticker'], 100 ) )
symbol_strings = []
 
for i in range (0, len ( symbol_groups )):
     symbol_strings.append (','.join(symbol_groups[i]))

#batch request API, import into Data Table     
for symbol_string in symbol_strings:
    
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}/&types=price,stats&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    
    
    try:
        for symbol in symbol_string.split(','):
             
            hqm_dataframe = hqm_dataframe.append(
                   pd.Series([
                      symbol, 
                      data[symbol]['price'],
                      'N/A',
                      data[symbol]['stats']['year1ChangePercent'], 
                      data[symbol]['stats']['month6ChangePercent'], 
                      data[symbol]['stats']['month3ChangePercent'], 
                      data[symbol]['stats']['month1ChangePercent'], 
                      
                    ], index = hqm_columns ),
                   ignore_index=True
                   )
    except KeyError:
         continue
     
print("Data Table complete")

#Creating Percentiles and Momentum Scores

hqm_dataframe ['Rank 1 Yr'] = hqm_dataframe ['1 Year Return'].rank(ascending=False, pct = True)
hqm_dataframe ['Rank 6 Mo'] = hqm_dataframe ['6 Month Return'].rank(ascending=False, pct = True)
hqm_dataframe ['Rank 3 Mo'] = hqm_dataframe ['3 Month Return'].rank(ascending=False, pct = True)
hqm_dataframe ['Rank 1 Mo'] = hqm_dataframe ['1 Month Return'].rank(ascending=False, pct = True)
hqm_dataframe ['Momentum Score'] = hqm_dataframe.iloc[:, 7:11].mean(axis=1)

print("Rank complete")


 
 # Sort data from Momentum Score
 
hqm_dataframe.sort_values('Momentum Score', ascending = False , inplace = True)
hqm_dataframe = hqm_dataframe [:50]
hqm_dataframe.reset_index(inplace = True)

del hqm_dataframe['index']

 
print("""Sorting complete. Top 50 Stocks by Momentum Score
      """)
 
#define portfolio size
portfolio_size = input ( 'Enter the value of your portfolio. Number/decimals only: ' )
 
 
while not portfolio_size.isnumeric():
     print("Invalid input. Number/decimals only")
     portfolio_size = input ( 'Enter the value of your portfolio: ' )
   

val = float(portfolio_size)
position_size = val / len( hqm_dataframe.index )

#Number of shares for each position

for i in range (len(hqm_dataframe.index)):
    hqm_dataframe.loc[i,'Number of Shares'] = position_size // hqm_dataframe.loc[i,'Stock Price']
    
    
 
 
# Export data to Microsoft Excel
    
writer = pd.ExcelWriter('Momentum.xlsx', engine = 'xlsxwriter')

hqm_dataframe.to_excel(writer, 'Momentum.xlsx', index= False)

#format Excel

background_color = '#FFFFFF'

font_color = '#192841'

string_format = writer.book.add_format(
        {
         'bg_color': background_color,
         'font_color': font_color,
         'border': 1
             
                }
        )

dollar_format = writer.book.add_format(
        {
         'num_format': '[$$-409]#,##0.00', 
         'bg_color': background_color,
         'font_color': font_color,
         'border': 1
             
                }
        )


integer_format = writer.book.add_format(
        {
         'num_format': '0', 
         'bg_color': background_color,
         'font_color': font_color,
         'border': 1
             
                }
        )

percent_format = writer.book.add_format(
        {
         'num_format': '0.00%', 
         'bg_color': background_color,
         'font_color': font_color,
         'border': 1
             
                }
        )


# apply formats

column_format = {
        'A': ['Ticker', string_format],
        'B' : ['Stock Price', dollar_format],
        'C': ['Shares', integer_format],
        'D': ['Percents', percent_format],
        'E': ['Percents', percent_format],
        'F': ['Percents', percent_format],
        'G': ['Percents', percent_format],
        'H': ['Percents', percent_format],
        'I': ['Percents', percent_format],
        'J': ['Percents', percent_format],
        'K': ['Percents', percent_format],
        'L': ['Percents', percent_format],
        }
worksheet = writer.sheets['Momentum.xlsx']

for column in column_format:
    worksheet.set_column(f'{column}:{column}', 18, column_format[column][1])



writer.save()

print("Complete. Data saved to Excel File: Momentum")
 
 
 
