# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:15:19 2022

@author: medbz
"""

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

from secrets import IEX_CLOUD_API_TOKEN


# setting up data frame and stock list
print("Creating Data Table... ")
stocks = pd.read_csv (r'sp_500_stocks.csv')
my_columns = ['Ticker', 'Stock Price', 'Market Cap', 'Number of Shares']
final_dataframe = pd.DataFrame(columns = my_columns)

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

#batch request API     
for symbol_string in symbol_strings:
    
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    
    try:
        for symbol in symbol_string.split(','):
             
            final_dataframe = final_dataframe.append(
                   pd.Series([
                      symbol, 
                      data[symbol]['quote']['latestPrice'], 
                      data[symbol]['quote']['marketCap'], 
                      'N/A'
                    ], index = my_columns ),
                   ignore_index=True
                   )
    except KeyError:
         continue

    
#define portfolio size
portfolio_size = input ( 'Enter the value of your portfolio. Number/decimals only: ' )


while not portfolio_size.isnumeric():
    print("Invalid input. Number/decimals only")
    portfolio_size = input ( 'Enter the value of your portfolio: ' )
  
print("Complete. Data saved to Excel File: Recommended_Trades")
position_size = val / len( final_dataframe.index )


#Number of shares for each position

for i in range (len(final_dataframe.index)):
    final_dataframe.loc[i,'Number of Shares'] = position_size // final_dataframe.loc[i,'Stock Price']
 
 
# Export data to Microsoft Excel
    
writer = pd.ExcelWriter('Recommended_Trades.xlsx', engine = 'xlsxwriter')

final_dataframe.to_excel(writer, 'Recommended_Trades.xlsx', index= False)

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
         'num_format': '$ 0.00', 
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


# apply formats

column_format = {
        'A': ['Ticker', string_format],
        'B' : ['Stock Price', dollar_format],
        'C': ['Market Capitalization', dollar_format],
        'D': ['Number of Shares', integer_format]
        }
worksheet = writer.sheets['Recommended_Trades.xlsx']

for column in column_format:
    worksheet.set_column(f'{column}:{column}', 18, column_format[column][1])



writer.save()
