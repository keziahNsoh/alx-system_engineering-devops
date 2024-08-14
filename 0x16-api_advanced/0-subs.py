#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers if subreddit is valid, 0 otherwise.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent":
        "python:subreddit_subscriber_count:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        elif response.status_code == 302:  # Redirect status code
            # The subreddit may be invalid if we get a
            # redirect to a search page
            return 0
        else:
            # For any other status codes, consider it as invalid
            return 0
    except requests.RequestException:
        # Catch any requests-related exceptions and return 0
        return 0
