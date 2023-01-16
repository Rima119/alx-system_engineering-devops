#!/usr/bin/python3
'''
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        userId = argv[1]
        API_URL = 'https://jsonplaceholder.typicode.com'
        user_res = requests.get('{}/users/{}'.format(API_URL, userId)).json()
        todo_res = requests.get('{}/todos'.format(API_URL)).json()
        EMPLOYEE_NAME = user_res.get('name')
        tasks = list(filter(lambda x: x.get('userId') == userId, todo_res))
        completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
        NUMBER_OF_DONE_TASKS = len(completed_tasks)
        TOTAL_NUMBER_OF_TASKS = len(tasks)
        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
              TOTAL_NUMBER_OF_TASKS))
        for todo in completed_tasks:
            print('\t {}'.format(todo.get('title')))
