import pandas as pd
from Data import *
import yfinance as yf

class Equity:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.data = pd.Series()

    def get_data(self, start_date, end_date):
        data_df = yf.download(self.symbol, start=start_date, end=end_date)
        for index, row in data_df.iterrows():
            self.data[index] = Data(self.symbol, index, row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume'])
        return self.data
