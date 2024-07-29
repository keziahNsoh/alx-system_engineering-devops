#!/usr/bin/python3
"""
Fetches the TODO list data for a given employee and exports it to a JSON file.
"""

import json
import requests
import sys


def fetch_data(employee_id):
     """
    Fetches the TODO list data for the specified employee ID and exports
    it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
     # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = "{}users/{}".format(base_url, employee_id)
    todos_url = "{}todos?userId={}".format(base_url, employee_id)

    try:
        # Fetch user data
        user_response = requests.get(users_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        return user_data, todos_data
    except requests.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)


def export_to_json(employee_id, user_data, todos_data):
    filename = "{}.json".format(employee_id)
    data = {"USER": user_data, "TODO": todos_data}

    with open(filename, "w") as file:
        json.dump(data, file, indent=0)

    print("Data exported to {}".format(filename))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_data, todos_data = fetch_data(employee_id)
    export_to_json(employee_id, user_data, todos_data)


if __name__ == "__main__":
    main()
