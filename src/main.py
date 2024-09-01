import json
import anthropic

from src.tool_integrator import process_tool_call
from src.analyzer_tools import tools
from src.config import CFG


with open(CFG.api_key_path) as file:
    api_key = json.load(file)["key"]

client = anthropic.Client(api_key=api_key)


def analyze_stock(stock_code):
    """Main function to analyze a stock."""
    print(f"# Stock Analysis for {stock_code}")

    initial_message = f"""
Conduct a thorough analysis of {stock_code}'s stock performance and future outlook. Follow these steps:

1. Generate a stock graph for the past 90 days.
2. Retrieve the current stock price.
3. Gather and summarize relevant news from the past week.

Based on this information, provide a comprehensive analysis including:

a) Technical Analysis:
   - Identify key trends, support, and resistance levels from the stock graph.
   - Calculate and interpret important technical indicators (e.g., Moving Averages, RSI, MACD).

b) Fundamental Analysis:
   - Summarize recent financial performance and any notable events or announcements.
   - Assess the company's position within its industry and relative to competitors.

c) News Impact:
   - Analyze how recent news might affect the stock's short-term and long-term performance.
   - Identify any upcoming events or potential catalysts that could impact the stock.

d) Risk Assessment:
   - Evaluate potential risks and challenges facing the company and its stock.
   - Consider both company-specific and broader market/economic factors.

e) Future Outlook:
   - Provide a detailed 3-month outlook for the stock, considering all analyzed factors.
   - Discuss potential scenarios that could significantly impact the stock's performance.

f) Short-term Price Prediction:
   - Based on all available data, particularly recent news and market sentiment, predict the stock price for the next 3 trading days.
   - Provide a range for each day (e.g., "Day 1: $X - $Y") and explain the reasoning behind each prediction.

Ensure that your analysis is well-structured, data-driven, and provides actionable insights for potential investors. Clearly state any assumptions made and emphasize the inherent uncertainty in short-term stock predictions.
"""

    messages = [
        {
            "role": "user",
            "content": [{"type": "text", "text": initial_message}],
        }
    ]

    while True:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4000,
            tools=tools,
            messages=messages,
        )

        if response.stop_reason == "tool_use":
            tool_calls = [
                content for content in response.content if content.type == "tool_use"
            ]

            # Add assistant's response (including tool calls) to messages
            messages.append({"role": "assistant", "content": response.content})

            # Process tool calls and prepare user's response
            user_content = []
            graph_data = None
            for tool_call in tool_calls:
                result = process_tool_call(tool_call.name, tool_call.input)
                tool_result = {
                    "type": "tool_result",
                    "tool_use_id": tool_call.id,
                    "content": result,
                }
                user_content.append(tool_result)

                if tool_call.name == "generate_stock_graph":
                    graph_data = result

            # Add image content after all tool results
            if graph_data:
                try:
                    user_content.append(
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": graph_data,
                            },
                        }
                    )
                except Exception as e:
                    print(f"Error adding image content: {e}")

            # Add user's response with tool results to messages
            messages.append({"role": "user", "content": user_content})
        else:
            final_response = next(
                (block.text for block in response.content if hasattr(block, "text")),
                None,
            )
            print("## Claude's Analysis:")
            print(final_response)
            break

    return final_response


if __name__ == '__main__':
    print(analyze_stock("MSFT"))
