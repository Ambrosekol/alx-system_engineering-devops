#!/usr/bin/python3
"""
This is a program that works with the Reddit API
It prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """shows titles of the first 10 hot posts"""
    api = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = requests.get(api)
    if req.status_code == 200:
        data = req.json()
        titles = [item["title"] for item in data["data"]["children"]]
        for val in titles:
            print(val)
    elif req.status_code == 302:
        print("None")
    else:
        print("None")
