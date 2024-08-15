#!/usr/bin/python3
"""
Module Docs
"""
import requests


def top_ten(subreddit):
    """
    Function Docs
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    params = {
        'limit': 10
    }
    response = requests.get(f'{url}/r/{subreddit}/hot.json', headers=header, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
