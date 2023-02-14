from fastapi import APIRouter
import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

router = APIRouter(prefix='/rss')


def get_source(url):
    """Return the source code for the provided URL.

    Args:
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


@router.get("/rss-feed")
def view(url: str) -> dict:
    """Return a Pandas dataframe containing the RSS feed contents.

    Args:
        url (string): URL of the RSS feed to read.

    Returns:
        df (dataframe): Pandas dataframe containing the RSS feed contents.
    """

    # Tutorial -> https://practicaldatascience.co.uk/data-science/how-to-read-an-rss-feed-in-python

    # As mentioned in the tutorial, RSS feeds come in various dialects,
    # which you can determine by reading the XML declaration on the first line of the file.
    # Ours is written in the 2005 version of Atom: <rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">.

    # TODO: Ideally, this endpoint should work as a wrapper around different RSS feed versions, it should detect
    # TODO: the version and then parse it accordingly.
    # TODO: you could probably use the state machine design pattern in here

    # url = "https://practicaldatascience.co.uk/feed.xml"
    # https://www.djangoproject.com/rss/weblog/
    # http://feeds.bbci.co.uk/news/rss.xml
    # TODO: You could try and create automatic container generations in React into your page for every "item" in the news feed.

    response = get_source(url)

    df = pd.DataFrame(columns=['title', 'pubDate', 'guid', 'description'])

    with response as r:
        items = r.html.find("item", first=False)

        for item in items:
            title = item.find('title', first=True).text
            pubDate = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            description = item.find('description', first=True).text

            row = {'title': title, 'pubDate': pubDate, 'guid': guid, 'description': description}
            df = df.append(row, ignore_index=True)

    return df
