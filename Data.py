class Data:
    def __init__(self, symbol, date, open, high, low, close, adj_close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.volume = volume

    def __str__(self):
        return f"Symbol: {self.symbol}, Date: {self.date}, Open: {self.open}, High: {self.high}, Low: {self.low}, Close: {self.close}, Adj Close: {self.adj_close}, Volume: {self.volume}"
    