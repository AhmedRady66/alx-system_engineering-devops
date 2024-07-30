#!/usr/bin/python3
"""Script to export data in JSON format"""

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

    data_export = {
        user_id: [
            {
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            }
            for i in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)
