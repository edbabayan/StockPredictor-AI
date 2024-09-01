tools = [
    {
        "name": "get_stock_price",
        "description": "Retrieves the current stock price for a given ticker symbol.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "The Stock ticker symbol, e.g AAPL for Apple Inc."
                }
            },
            "required": ["ticker"]
        }
    },
    {
        "name": "get_news_summary",
        "description": "Searches for news using DuckDuckGo library and returns a formatted string of news articles",
        "input_schema": {
            "type": "object",
            "properties": {
                "keywords": {
                    "type": "string",
                    "description": "Keywords to search for news. e.g., Apple Inc technology"
                }
            },
            "required": ["keywords"]
        }
    },
    {
        "name": "generate_stock_graph",
        "description": "Generates a stock price graph for the given ticker and returns it as a base64 encoded string",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "The Stock ticker symbol, e.g AAPL for Apple Inc."
                },
                "days": {
                    "type": "integer",
                    "description": "Number of days of historical data to include in the graph"
                }
            },
            "required": ["ticker"]
        }
    }
]
