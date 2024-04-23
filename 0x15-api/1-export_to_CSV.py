#!/usr/bin/python3
"""
Gather data from an API
"""

import sys
import requests
import csv

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

if __name__ == '__main__':
    # create and save data in csv file
    with open("{}.csv".format(employee_id), "w", newline="") as fichier:
        writer = csv.writer(fichier, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
                ])
