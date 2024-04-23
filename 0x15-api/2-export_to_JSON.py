#!/usr/bin/python3
"""Gather data from an API"""

import sys
import requests
import csv
import json

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

# get employee name
employee_name = employee.get("username")

# filter completed task
completed = []
for todo in todo_list:
    if todo.get('completed') is True:
        completed.append(todo.get('title'))

x_completed = len(completed)
x_todos = len(todo_list)

# Transform json format
taks_list = [
    {
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": employee_name
    } for task in todo_list
]

json_format = {employee_id: taks_list}

if __name__ == '__main__':
    # create and save data in csv file
    with open("{}.json".format(employee_id), "w") as fichier:
        json.dump(json_format, fichier, indent=4)
