#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit"""
    header = {
            'User-Agent': 'My-User-Agent'
            }
    url = 'https://reddit.com/r/{}/top.json'.format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        post_list = response.json()['data']['children'
        for idx, post in enumerate(post_list):
            print(post['data']['title'])
            if idx == 9:
                break
    else:
        print('None')
