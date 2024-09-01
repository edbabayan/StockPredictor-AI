import io
import base64
from matplotlib import pyplot as plt

from src.data_retrieval import get_stock_data


def generate_stock_graph(ticker, days=90):

    stock_data = get_stock_data(ticker, days)

    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'], label='Closing Price')
    plt.title(f"{ticker} Stock Price - Last {days} Days")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    image_base64 = base64.b64encode(buffer.getvalue()).decode('ascii')

    return image_base64
