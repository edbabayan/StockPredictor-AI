import yfinance as yf
from datetime import datetime, timedelta


def get_stock_data(ticker, days=90):
    """
    Fetches historical stock data for a given ticker symbol over a specified number of days.

    Args:
        ticker (str): The stock ticker symbol to fetch data for (e.g., 'AAPL' for Apple).
        days (int, optional): The number of days of historical data to retrieve.
                              Defaults to 90 days.

    Returns:
        pandas.DataFrame: A DataFrame containing the stock's historical data including
                          Open, High, Low, Close, Volume, and Adjusted Close prices
                          for each day within the specified range.

        str: A message indicating that no data was found if the ticker symbol is invalid
             or no data is available for the given date range.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    if stock_data.empty():
        return f"No stock data found for {ticker}"
    return stock_data

