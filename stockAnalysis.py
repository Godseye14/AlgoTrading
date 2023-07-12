import pandas as pd
pd.options.display.float_format = '{:.4f}'.format

from algoTradingKit import *

symbol = input("Enter symbol : ")
start = input("Start Date : ")
end = input("End Date : ")

if len(symbol)==0 and len(start)==0 and len(end)==0:
    print("User Input not provided correctly.. Taking Bajaj Finance as default script...")
    symbol = "BAJFINANCE.NS"
    start = "2003-05-26"
    end = "2023-07-12"

df = get_data(symbol,start,end)
if len(df)!=0:
    close = get_close(df)
    close = get_returns(close)
    save_to_csv(symbol,start,end,close)

df = load_csv()
if len(df)!=0:
    cagr = get_cagr(df)