#!/usr/bin/python3
"""
    Gather data from an API
    using requests
"""

import sys
import requests


base_url = "https://jsonplaceholder.typicode.com"
employee_id = sys.argv[1]

# get employee
employee = requests.get("{}/users/{}".format(
    base_url, employee_id)).json()

# get todo list
todo_list = requests.get(
    "{}/todos".format(base_url),
    {"userId": employee_id}
    ).json()

# filter completed task
completed = []
for todo in todo_list:
    if todo.get('completed') is True:
        completed.append(todo.get('title'))

x_completed = len(completed)
x_todos = len(todo_list)

if __name__ == '__main__':
    # display employee name
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), x_completed, x_todos)
        )

    # displays tasks
    for task in completed:
        print("\t{}".format(task))
