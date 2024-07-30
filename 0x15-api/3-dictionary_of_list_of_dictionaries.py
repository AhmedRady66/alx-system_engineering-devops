#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests


def fetch_user_data():
    """Get user information and to-do lists for all employee"""
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    data_export = {}

    for user in users:
        user_id = user["id"]
        todos_response = requests.get(url + f"todos?userId={user_id}")
        todo_list = todos_response.json()

        data_export[user_id] = []

        for todo in todo_list:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }

            data_export[user_id].append(task_info)

    return data_export


if __name__ == "__main__":
    data_export = fetch_user_data()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)
