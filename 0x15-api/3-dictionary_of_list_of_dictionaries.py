#!/usr/bin/python3
""" script to export data in the JSON format """
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    user_name = requests.get(url, verify=False).json()
    list_tasks = {}
    for user in user_name:
        todos = requests.get(url + '/{}/todos'.format(user['id'])).json()
        list_tasks[user['id']] = [{'task': task.get('title'),
                                   'completed': task.get('completed'),
                                   'username': user['username']}
                                  for task in todos]
    with open("todo_all_employees.json", 'w', newline='') as jsonfile:
        json.dump(list_tasks, jsonfile)
