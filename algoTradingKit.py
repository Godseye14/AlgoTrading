import numpy as np
import pandas as pd
pd.options.display.float_format = '{:.4f}'.format
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

def get_data(symbol,start,end):
        """
        Fetch data from yfinance
        Params - 
        symbol : Script name in yahoo finance
        start : start date
        end : end date
        Returns -
        dataframe
        """
        df = yf.download(symbol,start,end)
        return df

def get_close(df):
        """
        This function is used to get the close from dataframe and rename the column to Price
        Param -
        df : dataframe
        Returns -
        dataframe
        """
        close = df.Close.dropna().to_frame().copy()
        close.rename(columns={"Close":'Price'},inplace=True)
        print("Got Close values from df, Renaming it to Price...")
        return close

def get_returns(close):
        close['Returns'] = close.Price.pct_change(periods=1)
        print('Calculated Returns, New dataFrame is :')
        print(close)
        return close

def save_to_csv(symbol,start,end,df):
        df.to_csv(symbol+'--'+start+'--'+end+'.csv')
        print("File saved as :",symbol+'--'+start+'--'+end+'.csv')

def get_df(path):
        """
        Load csv file
        """
        df = pd.read_csv(path,index_col='Date',parse_dates=['Date'])
        return df

def load_csv():
        symbol = input("Enter symbol : ")
        start = input("Start Date : ")
        end = input("End Date : ")
        path=symbol+'--'+start+'--'+end+'.csv'
        try:
                df = pd.read_csv(path,index_col='Date',parse_dates=['Date'])
                print('Loaded csv file...')
                return df
        except Exception as err:
                print(err)

def get_cagr(df):
        multiple = df.Price[-1]/df.Price[0]
        start=df.index[0]
        end=df.index[-1]
        timeDiff = end - start
        timeDiffInYears = timeDiff.days/365.25
        cagr = multiple**(1/timeDiffInYears)-1
        print(f"CAGR for the selected script b/w {start} and {end} is : {cagr}")
        print(f"CAGR in percentage is : {cagr*100}")
        return cagr