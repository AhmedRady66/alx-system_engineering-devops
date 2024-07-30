#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    # Check if user_id is a list of dictionaries
    if isinstance(todos, list) and all(isinstance(i, dict) for i in todos):
        print("USER_ID's value type is a list of dicts: OK")

        data_export = {user_id: []}

        for i in todos:
            task_info = {
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            }
            data_export[user_id].append(task_info)

        if len(data_export[user_id]) == len(todos):
            print("All tasks found: OK")

        with open("{}.json".format(user_id), "w") as jsonfile:
            json.dump(data_export, jsonfile, indent=4)
    else:
        print("USER_ID's value is not a list of dicts")
