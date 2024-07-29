#!/usr/bin/python3
"""Write a Python script that, using this https://jsonplaceholder.typicode.com/
for a given employee ID
returns information about his/her TODO list progress."""


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    emp_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(emp_id))
    user = user_response.json()

    params = {"userId": emp_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    completed = []

    for i in todos:
        if i.get("completed") is True:
            completed.append(i.get("title"))
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(completed), len(todos)))

    for j in completed:
        print("\t {}".format(j))
