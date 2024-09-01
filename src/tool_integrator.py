from src.live_stock_news import get_news_summary
from src.data_retrieval import get_stock_data
from src.stock_plot import generate_stock_graph


def process_tool_call(tool_name, tool_input):
    """
    Processes a tool call by determining which specific function to execute based on the tool name.

    This function acts as a dispatcher, executing different functions depending on the specified `tool_name`.
    It supports fetching the latest stock price, summarizing news articles, and generating a stock graph.
    The corresponding function is executed based on the tool name provided, and the result is displayed and returned.

    Args:
        tool_name (str): The name of the tool or function to execute. Supported values are:
            - "get_stock_price": Fetches the latest stock price for a given ticker symbol.
            - "get_news_summary": Fetches and summarizes news articles based on provided keywords.
            - "generate_stock_graph": Generates and displays a stock price graph for a given ticker symbol.
        tool_input (dict): A dictionary containing the input parameters required by the selected tool.
            Expected keys depend on the tool:
            - For "get_stock_price": {"ticker": str}
            - For "get_news_summary": {"keywords": str}
            - For "generate_stock_graph": {"ticker": str, "days": int (optional)}

    Returns:
        str: The result of the executed function, either as a formatted string of the latest stock price,
             a summary of news articles, or a message indicating an unknown tool.

    Notes:
        - The function displays the result using Markdown for better formatting in a notebook environment.
        - If an unknown `tool_name` is provided, the function returns "Unknown function".
    """
    if tool_name == "get_stock_price":
        stock_data = get_stock_data(tool_input["ticker"])
        latest_price = stock_data['Close'].iloc[-1]
        result = f"The latest closing price for {tool_input['ticker']} is ${latest_price}"
        print(f"**Current Stock Price ** {result}")
        return result
    elif tool_name == "get_news_summary":
        result = get_news_summary(tool_input["keywords"])
        print("**Recent News**")
        print(result)
        return result
    elif tool_name == "generate_stock_graph":
        generate_stock_graph(tool_input["ticker"], tool_input.get("days", 90))
    else:
        return "Unknown function"
