#!/usr/bin/python3
"""Docstring"""
import requests


def recurse(subreddit, after=None, titles=[]):
    """
    Recursively queries the Reddit API and returns a list of hot article.

    Args:
        subreddit (str): The name of the subreddit to query.
        limit (int): The maximum number of articles to get (default is 10).
        after (str): ID of the last article gotten (used for pagination).
        titles (list): Store the article titles (default is an empty list).

    Returns:
        list: Article titles giving subreddit,or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]

        for article in articles:
            titles.append(article["data"]["title"])

        after = data["data"]["after"]

        if after is not None:
            return recurse(subreddit, after, titles)
        else:
            return titles
    else:
        return None
