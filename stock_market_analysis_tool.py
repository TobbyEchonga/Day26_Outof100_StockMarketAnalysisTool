import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class StockMarketAnalysisTool:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = None

    def fetch_stock_data(self):
        try:
            # Fetch historical stock data using yfinance
            self.stock_data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            print("Stock data fetched successfully.")
        except Exception as e:
            print(f"Error fetching stock data: {e}")

    def plot_stock_prices(self):
        if self.stock_data is not None:
            # Plot stock closing prices
            plt.figure(figsize=(10, 5))
            plt.plot(self.stock_data['Close'], label=f"{self.ticker} Closing Prices")
            plt.title(f"{self.ticker} Stock Prices")
            plt.xlabel("Date")
            plt.ylabel("Closing Price (USD)")
            plt.legend()
            plt.show()
        else:
            print("No stock data available. Please fetch data first.")

    def analyze_stock(self):
        if self.stock_data is not None:
            # Perform basic analysis (e.g., calculate daily returns)
            self.stock_data['Daily_Return'] = self.stock_data['Close'].pct_change()

            # Display basic statistics
            print("\nBasic Stock Analysis:")
            print(self.stock_data[['Close', 'Daily_Return']].describe())

        else:
            print("No stock data available. Please fetch data first.")

def get_user_date_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            date_obj = datetime.strptime(user_input, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

def main():
    # Get user input for stock symbol
    ticker = input("Enter stock symbol (e.g., AAPL): ")

    # Get user input for start date
    start_date = get_user_date_input("Enter start date (YYYY-MM-DD): ")

    # Get user input for end date (ensuring it's not before the start date)
    while True:
        end_date = get_user_date_input("Enter end date (YYYY-MM-DD): ")
        if end_date >= start_date:
            break
        else:
            print("End date must be on or after the start date. Please enter a valid date.")

    # Create an instance of the StockMarketAnalysisTool
    stock_analysis_tool = StockMarketAnalysisTool(ticker, start_date, end_date)

    # Fetch stock data
    stock_analysis_tool.fetch_stock_data()

    # Plot stock prices
    stock_analysis_tool.plot_stock_prices()

    # Analyze stock
    stock_analysis_tool.analyze_stock()

if __name__ == "__main__":
    main()
