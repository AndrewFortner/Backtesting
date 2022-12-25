from datetime import datetime

class Trade:
    def __init__(self, equity, data, timestamp, profit, price, strategy):
        self.symbol = equity.symbol
        self.data = data
        self.day = timestamp.date()
        self.time = timestamp.time()
        self.profit = profit
        self.percent_profit = profit * 100 / price
        self.equity = equity
        self.strategy = strategy

    def __str__(self):
        return f"Strategy: {self.strategy}, Symbol: {self.symbol}, Date: {self.day}, Time: {self.time}, Profit: {self.profit}, Percent Profit: {self.percent_profit}"