#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """Print the titles of the 10 hot posts"""
    req = requests.get(
        'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"}
        ).json()

    try:
        for res in req.get("data").get("children"):
            title = res.get("data").get('title')
            print(title)
    except Exception as e:
        print(None)
