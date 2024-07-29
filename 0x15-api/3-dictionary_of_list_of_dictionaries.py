#!/usr/bin/python3
"""
Fetches the TODO list data for all employees and exports it to a JSON file.
"""

import json
import requests
import sys


def fetch_all_data():
    """
    Fetches the TODO list data for all employees and exports it to a JSON file.
    """
    # Define the API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch users data
    try:
        users_response = requests.get(users_url)
        users_response.raise_for_status()  # Raise HTTPError for bad responses
        users_data = users_response.json()
    except requests.RequestException as e:
        print("Error fetching users data: {}".format(e))
        sys.exit(1)

    # Fetch TODO data
    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()  # Raise HTTPError for bad responses
        todos_data = todos_response.json()
    except requests.RequestException as e:
        print("Error fetching TODO data: {}".format(e))
        sys.exit(1)

    # Prepare data for export
    export_data = {}
    for user in users_data:
        user_id = str(user["id"])
        username = user["username"]
        tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos_data if todo["userId"] == user["id"]
        ]
        export_data[user_id] = tasks

    # Write data to JSON file
    filename = "todo_all_employees.json"
    try:
        with open(filename, "w") as file:
            json.dump(export_data, file, indent=4)
    except IOError as e:
        print("Error writing to file: {}".format(e))
        sys.exit(1)

    print("Data successfully exported to {}".format(filename))


if __name__ == "__main__":
    fetch_all_data()
