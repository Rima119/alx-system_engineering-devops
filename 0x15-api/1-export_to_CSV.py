#!/usr/bin/python3
""" script to export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todos = requests.get(url.format(userId), verify=False).json()
    url = "https://jsonplaceholder.typicode.com/users/{}"
    user_name = requests.get(url.format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([int(userId), user_name.get('username'),
                task.get('completed'), task.get('title')])
