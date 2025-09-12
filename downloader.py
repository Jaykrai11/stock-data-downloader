
import yfinance as yf
import pandas as pd

ticker ='AAPL'
start_date='2020-01-01'
end_date='2024-01-01'

data= yf.download(ticker,start=start_date,end=end_date)

print(data.head())

data.to_csv(f'{ticker}_stock_data.csv',index=True)

print(f"Stock data of {ticker}_stock_data.csv saved successfully")

