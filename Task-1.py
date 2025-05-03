import pandas as pd
import datetime
import time
import yfinance as yf

ticker = yf.Ticker("TSLA")
## startdate = datetime.datetime(2025, 2, 1) ##
## enddate   = datetime.datetime(2025, 5, 1)
ticker.info
hist  = ticker.history(period="1mo") 

print(hist)

def get_stock_history(ticker, startdate, enddate, interval)->pd.DataFrame:

    print(get_stock_history)
    
