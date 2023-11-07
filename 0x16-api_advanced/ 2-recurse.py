#!/usr/bin/python3
"""
This is a program that works with the Reddit API
It prints the titles of the first 10 hot posts
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    # Initialize hot_list as an empty list on the first call
    if hot_list is None:
        hot_list = []

    # Define the Reddit API endpoint for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Include 'after' parameter to paginate through results
    if after:
        url += f"&after={after}"

    # Set a custom User-Agent header to avoid API access issues
    headers = {'User-Agent': 'MyRedditApp/1.0'}

    # Make the GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is valid (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            # If no posts are found, return None
            return None
        else:
            # Add the titles of the current page of hot posts to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Recursively call the function with the 'after'
            next_page = data.get('data', {}).get('after')
            if next_page:
                return recurse(subreddit, hot_list, next_page)
            else:
                return hot_list
    elif response.status_code == 302:
        # If the subreddit is invalid and results in a redirect, return None
        return None
    else:
        # Handle other possible errors if needed
        print(f"Error: {response.status_code}")
        return None
