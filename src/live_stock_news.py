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
    Fetch and summarize news articles based on specified keywords.

    This function retrieves news articles using the DuckDuckGo Search (DDGS) API based on the provided keywords.
    The articles are then formatted into a DataFrame with relevant details such as the publication date, title,
    source, and body. Additionally, the article images are converted into HTML image tags for display. The function
    returns a summary string that compiles key information from each article.

    Args:
        keywords (str): The search terms used to find relevant news articles.
        max_results (int, optional): The maximum number of articles to fetch. Defaults to 10.

    Returns:
        str: A string containing a summary of each article, including the date, title, source, and a brief body of the news.

    Notes:
        - The function fetches articles from the past week.
        - The DataFrame created includes columns for the date, an image in HTML format, title, source, and body.
        - The returned summary is a string that consolidates essential details from the articles.
    """
    with DDGS() as ddgs:
        news_gen = ddgs.news(keywords, region="wt-wt", safesearch="off", timelimit="w", max_results=max_results)
        news_articles = list(news_gen)

    df = pd.DataFrame(news_articles)

    # Apply the function to the 'image' column
    df['image'] = df['image'].apply(image_html)

    # Select and reorder columns
    df = df[['date', 'image', 'title', 'source', 'body']]

    # Create summary string
    summary = ""
    for _, article in df.iterrows():
        summary += f"Date: {article['date']}\nTitle: {article['title']}\nSource: {article['source']}\nSummary: {article['body']}\n\n"

    return summary
