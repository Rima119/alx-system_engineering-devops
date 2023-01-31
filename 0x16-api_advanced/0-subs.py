#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    header = {
            'User-Agent': 'My-User-Agent'
            }
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
