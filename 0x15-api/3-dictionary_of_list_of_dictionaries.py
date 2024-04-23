#!/usr/bin/python3
"""Gather data from an API"""

import sys
import requests
import csv
import json

base_url = "https://jsonplaceholder.typicode.com"

# get all employees
employees = requests.get("https://jsonplaceholder.typicode.com/users").json()

# get all todos
todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

data = {
    employee.get('id'): [
        {
            "username": employee.get('username'),
            "task": task.get('title'),
            "completed": task.get("completed")
        } for task in todos if task.get('userId') == employee.get('id')
    ] for employee in employees
}

if __name__ == '__main__':
    # create and save data in csv file
    with open("todo_all_employees.json", "w") as fichier:
        json.dump(data, fichier, indent=4)
