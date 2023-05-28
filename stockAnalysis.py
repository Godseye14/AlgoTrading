import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
pd.options.display.float_format = '{:.4f}'.format
import yfinance as yf

from algoTradingKit import *

# symbol = input("Enter symbol : ")
# start = input("Start Date : ")
# end = input("End Date : ")

# df = get_data(symbol,start,end)

# close = get_close(df)

# close = get_returns(close)

# save_to_csv(symbol,start,end,close)

df = load_csv()

cagr = get_cagr(df)