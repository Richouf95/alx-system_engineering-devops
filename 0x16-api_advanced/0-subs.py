#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """Number of subscribers"""
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False)
    if req.status_code == 200:
        res = req.json()
        subscribers = res['data']['subscribers']
        return subscribers
    else:
        return 0
