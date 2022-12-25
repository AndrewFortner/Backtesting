import Trade
import Equity
import Data

class Stats:
    def __init__(self, trades):
        self.trades = trades
        self.profit = 0
        self.percent_profit = 0
        self.profit_per_trade = 0
        self.percent_profit_per_trade = 0
        self.percent_profit_annualized = 0
        self.maximum_drawdown = 0
        self.largest_losing_streak = 0
        self.largest_winning_streak = 0
        self.percentage_of_profitable_trades = 0
        self.std = 0
        self.sharpe = 0
        self.calculate()

    def calculate(self):
        for trade in self.trades:
            self.profit += trade.profit
            self.percent_profit += trade.percent_profit
        self.profit_per_trade = self.profit / len(self.trades)
        self.percent_profit_per_trade = self.percent_profit / len(self.trades)
        self.percent_profit_annualized = ((1 + self.percent_profit_per_trade/100) ** 252 - 1) * 100
        self.maximum_drawdown = self.calculate_maximum_drawdown()
        self.largest_losing_streak = self.calculate_largest_losing_streak_value()
        self.largest_winning_streak = self.calculate_largest_winning_streak_value()
        self.percentage_of_profitable_trades = len([trade for trade in self.trades if trade.percent_profit > 0]) / len(self.trades)
        self.std = self.calculate_std()
        self.sharpe = self.calculate_sharpe()

    def calculate_maximum_drawdown(self):
        maximum_drawdown = 0
        for trade in self.trades:
            if trade.percent_profit < maximum_drawdown:
                maximum_drawdown = trade.percent_profit
        return maximum_drawdown

    def calculate_largest_losing_streak_value(self):
        largest_losing_streak = 0
        current_losing_streak = 0
        for trade in self.trades:
            if trade.percent_profit < 0:
                current_losing_streak += trade.percent_profit
            else:
                if current_losing_streak < largest_losing_streak:
                    largest_losing_streak = current_losing_streak
                current_losing_streak = 0
        return largest_losing_streak

    def calculate_largest_winning_streak_value(self):
        largest_winning_streak = 0
        current_winning_streak = 0
        for trade in self.trades:
            if trade.percent_profit > 0:
                current_winning_streak += trade.percent_profit
            else:
                if current_winning_streak > largest_winning_streak:
                    largest_winning_streak = current_winning_streak
                current_winning_streak = 0
        return largest_winning_streak

    def calculate_std(self):
        sum_of_difference_squared = 0
        for trade in self.trades:
            sum_of_difference_squared += (trade.percent_profit - self.percent_profit_per_trade) ** 2
        return (sum_of_difference_squared / (len(self.trades) - 1)) ** 0.5

    def calculate_sharpe(self):
        return (self.percent_profit_annualized - 3.77) / self.calculate_std()

    def __str__(self):
        return f"Profit: {self.profit}, Percent Profit: {self.percent_profit}, Profit Per Trade: {self.profit_per_trade}, Percent Profit Per Trade: {self.percent_profit_per_trade}, Percent Profit Annualized: {self.percent_profit_annualized}, Maximum Drawdown: {self.maximum_drawdown}, Largest Losing Streak: {self.largest_losing_streak}, Largest Winning Streak: {self.largest_winning_streak}, Percentage of Profitable Trades: {self.percentage_of_profitable_trades}, Std: {self.std}, Sharpe: {self.sharpe}"