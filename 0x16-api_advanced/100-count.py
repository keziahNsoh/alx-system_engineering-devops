#!/usr/bin/python3
"""Docstring for count_words function."""
import requests

def count_words(subreddit, word_list, word_count=None, after=None):
    """Count the number of words in the titles of hot articles that are in the list of words."""
    
    if word_count is None:
        word_count = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]
        
        for article in articles:
            title = article["data"]["title"].split()
            
            for word in word_list:
                count = 0
                for title_word in title:
                    if word.lower() == title_word.lower():
                        count += 1
                
                if count > 0:
                    if word.lower() not in word_count:
                        word_count[word.lower()] = count
                    else:
                        word_count[word.lower()] += count
        
        after = data["data"]["after"]
        
        if after is None:
            return word_count
        else:
            return count_words(subreddit, word_list, word_count, after)
    else:
        return word_count
