#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_article = hot_list + [hot.get("data").get("title")
                        for hot in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()
    if not info.get("data").get("after"):
        return hot_article

    return recurse(subreddit, hot_article, info.get("data").get("count"),
                   info.get("data").get("after"))
