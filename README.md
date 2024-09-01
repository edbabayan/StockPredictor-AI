# StockPredictor-AI

StockPredictor-AI is a Python-based tool that utilizes live stock prices, historical data, and the Claude 3.5 LLM model to provide comprehensive stock analysis and predictions. It helps investors by offering detailed insights and forecasts for informed decision-making.

## Features

- **Real-time Stock Data**: Retrieve current stock prices using ticker symbols.
- **Historical Data Analysis**: Analyze up to 90 days of historical stock data.
- **Stock Predictions**: Forecast future stock movements with advanced AI models.
- **News Summary**: Gather and summarize relevant news articles about specific stocks.
- **Comprehensive Analysis**: Includes technical and fundamental analysis, news impact assessment, risk evaluation, and short-term price predictions.

## Functions

### `analyze_stock(stock_code)`

Conducts a thorough analysis of a stock including:
- Generating a stock graph for the past 90 days.
- Retrieving the current stock price.
- Summarizing recent news.
- Performing technical and fundamental analysis.
- Assessing news impact and risks.
- Providing a 3-month outlook and short-term price predictions.

### `get_stock_data(ticker, days=90)`

Fetches historical stock data for a given ticker symbol and number of days. Returns a DataFrame or an error message if no data is found.

### `get_news_summary(keywords, max_results=10)`

Retrieves and summarizes the latest news articles based on provided keywords. Returns a formatted string with news summaries.

### `generate_stock_graph(ticker, days=90)`

Generates a stock price graph for a given ticker symbol over a specified number of days. Returns a base64 encoded string of the generated graph.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/StockPredictor-AI.git
   cd StockPredictor-AI
   ```
   
2. **Add anthropic api key to the root directory**
   ```yaml
    {"key": "anthropic_api_key"}
   ```
3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the main.py file**
   ```bash
   python main.py
   ```