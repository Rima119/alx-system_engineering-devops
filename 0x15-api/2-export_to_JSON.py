#!/usr/bin/python3
""" script to export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todos = requests.get(url.format(userId), verify=False).json()
    url = "https://jsonplaceholder.typicode.com/users/{}"
    user_name = requests.get(url.format(userId), verify=False).json()
    list_tasks = {userId: [{'task': task.get('title'), 'completed':
                  task.get('completed'), 'username': user_name['username']}
                  for task in todos]}
    with open("{}.json".format(userId), 'w', newline='') as jsonfile:
        json.dump(list_tasks, jsonfile)
