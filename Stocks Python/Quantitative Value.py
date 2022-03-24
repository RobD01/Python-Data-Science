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





# setting up data frame and stock list
print("Creating Data Table... ")
stocks = pd.read_csv (r'sp_500_stocks.csv')


# Advanced Momentum
my_columns = [
        'Ticker', 
        'Stock Price', 
        'PE Ratio',
        'PEG Ratio',
        'PS Ratio',
        'Market Cap',
        'Number of Shares',
        'Company Name'

        ]

value_dataframe = pd.DataFrame(columns = my_columns)

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
    
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}/&types=quote,price,advanced-stats,stats&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    
    
    try:
        for symbol in symbol_string.split(','):
             
            value_dataframe = value_dataframe.append(
                   pd.Series([
                      symbol, 
                      data[symbol]['price'],
                      data[symbol]['quote']['peRatio'],
                      data[symbol]['advanced-stats']['pegRatio'],
                      data[symbol]['advanced-stats']['priceToSales'],
                      data[symbol]['quote']['marketCap'], 
                      'N/A',
                      data[symbol]['stats']['companyName']

                    ], index = my_columns ),
                   ignore_index=True
                   )
    except KeyError:
         continue
     
print("Data Table complete")

 # Sort and Filter data by top 50 Market Cap
value_dataframe.sort_values('Market Cap', ascending = False , inplace = True)
value_dataframe = value_dataframe [:50]
print("Filtered Top 50 by Market Cap")

# Sort data by lowest Price Sales Ratio
value_dataframe.sort_values('PS Ratio', ascending = True , inplace = True)
value_dataframe.reset_index(inplace = True)

del value_dataframe['index']

print("""Sorting complete. Ordered by lowest Price / Sales Ratio
      """)

#define portfolio size
portfolio_size = input ( 'Enter the value of your portfolio. Number/decimals only: ' )
 
 
while not portfolio_size.isnumeric():
     print("Invalid input. Number/decimals only")
     portfolio_size = input ( 'Enter the value of your portfolio: ' )
   

val = float(portfolio_size)

if val < 10000:
    print("Computer says: Those OTM dailies working well!")
    
elif val < 40000:
    print("Computer says: I think Wendy's is hiring")
else:
    print("Computer says: Money Printer go brrrrr")

position_size = val / len( value_dataframe.index )

#Number of shares for each position

for i in range (len(value_dataframe.index)):
    value_dataframe.loc[i,'Number of Shares'] = position_size // value_dataframe.loc[i,'Stock Price']
    
    
 
 
# Export data to Microsoft Excel
    
writer = pd.ExcelWriter('Value.xlsx', engine = 'xlsxwriter')

value_dataframe.to_excel(writer, 'Value.xlsx', index= False)

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

float_format = writer.book.add_format(
        {
         'num_format': '0.00', 
         'bg_color': background_color,
         'font_color': font_color,
         'border': 1
             
                }
        )


# apply formats

column_format = {
        'A': ['Ticker', string_format],
        'B' : ['Stock Price', dollar_format],
        'C': ['Ratio', float_format],
        'D': ['Ratio', float_format],
        'E': ['Ratio', float_format],
        'F': ['Market Cap', dollar_format],
        'G': ['Shares', integer_format],
        'H': ['Company Name', string_format]

        }
worksheet = writer.sheets['Value.xlsx']

for column in column_format:
    worksheet.set_column(f'{column}:{column}', 18, column_format[column][1])



writer.save()

print("Complete. Data saved to Excel File: Value")

print("""Computer says: remember to diamond hand

                                                                                        
                          ██████████████████████████████████████                        
                        ██▒▒██    ░░██  ██    ░░██▒▒██    ░░██▓▓██                      
                      ██▒▒  ░░██░░██    ░░██░░██▒▒  ░░██░░██▓▓  ▓▓██                    
                    ██▒▒  ░░  ░░██    ░░  ░░██▒▒  ░░  ░░██▓▓  ▓▓  ▓▓██                  
                    ██████████████████████████████████████████████████                  
                    ██▒▒▒▒▒▒▒▒░░██        ░░██▒▒▒▒▒▒▒▒░░██▓▓▓▓▓▓▓▓▓▓██                  
                      ██▒▒  ░░░░██      ░░░░██▒▒    ░░░░██▓▓  ▓▓▓▓██                    
                        ██▒▒  ░░░░██    ░░░░██▒▒  ░░░░██▓▓  ▓▓▓▓██                      
                          ██▒▒  ░░██    ░░░░██▒▒  ░░░░██▓▓  ▓▓██                        
                            ██▒▒  ░░██  ░░░░██▒▒  ░░██▓▓  ▓▓██                          
                              ██▒▒░░██  ░░░░██▒▒  ░░██▓▓▓▓██                            
        ░░      ░░              ██▒▒░░██  ░░██▒▒░░██▓▓▓▓██                ░░      ░░    
                                  ██▒▒██  ░░██▒▒░░██▓▓██  ░░                            
                                    ██▒▒██░░██▒▒██▓▓██                                  
                                      ████░░██▒▒████                                    
                                    ░░  ██░░██▒▒██        ░░                            
                                          ██████                                        
                                                                                        
 
░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░

    """)