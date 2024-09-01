import pandas as pd
from IPython.display import display, HTML
from duckduckgo_search import DDGS


def image_html(url):
    """
    Generates an HTML <img> tag for displaying an image with the specified URL.

    Args:
        url (str): The URL of the image to be displayed.

    Returns:
        str: An HTML string containing the <img> tag with inline styles to limit the image size.
    """
    return f'<img src="{url}" style="max-width:100px; max-height:100px;">'


def get_news_summary(keywords, max_results=10):
    """
    Fetches news articles based on given keywords and returns a summary of the news.

    This function uses the DuckDuckGo Search (DDGS) API to retrieve news articles related to the specified keywords.
    The retrieved articles are formatted into a DataFrame, including an HTML image tag for displaying images. The
    function returns a summary string containing key information about each article.

    Args:
        keywords (str): Keywords or search terms used to fetch news articles.
        max_results (int, optional): The maximum number of news articles to retrieve. Defaults to 10.

    Returns:
        str: A summary string containing the date, title, source, and body of each news article.

    Notes:
        - The news articles are fetched from the past week.
        - The resulting DataFrame displays the date, image (as an HTML tag), title, source, and body of the articles.
    """
    with DDGS() as ddgs:
        news_gen = ddgs.news(keywords, region="wt-wt", safesearch="off", timelimit="w", max_results=max_results)
        news_articles = list(news_gen)

    df = pd.DataFrame(news_articles)

    # Apply the function to the 'image' column
    df['image'] = df['image'].apply(image_html)

    # Select and reorder columns
    df = df[['date', 'image', 'title', 'source', 'body']]

    # Display the DataFrame
    display(HTML(df.to_html(escape=False)))

    # Create summary string
    summary = ""
    for _, article in df.iterrows():
        summary += f"Date: {article['date']}\nTitle: {article['title']}\nSource: {article['source']}\nSummary: {article['body']}\n\n"

    return summary

