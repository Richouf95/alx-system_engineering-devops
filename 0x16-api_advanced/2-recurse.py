#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no data are found for the given subreddit,
the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list containing the titles of all 
    hot articles for a givensubreddit.
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot/.json".format(subreddit),
        headers={"User-Agent": "Toi"},
        params={
            "after": after,
            "count": count,
            "limit": 100
        },
        allow_redirects=False).json()

    data = res.get("data")
    after = data.get("after")
    count += data.get("dist")

    for title in data.get("children"):
        hot_list.append(title.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list