#!/usr/bin/python3
"""
Fetches the TODO list data for a given employee and exports it to a JSON file.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Fetches the TODO list data for the specified employee ID and exports
    it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Define the API endpoints
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id
    )

    # Fetch employee data
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise HTTPError for bad responses
        user_data = user_response.json()
    except requests.RequestException as e:
        print("Error fetching user data: {}".format(e))
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
    user_name = user_data.get("username", "Unknown")
    tasks = [
        {"task": todo["title"], "completed": todo["completed"], "username": user_name}
        for todo in todos_data
    ]
    export_data = {str(employee_id): tasks}

    # Write data to JSON file
    filename = "{}.json".format(employee_id)
    try:
        with open(filename, "w") as file:
            json.dump(export_data, file, indent=4)
    except IOError as e:
        print("Error writing to file: {}".format(e))
        sys.exit(1)

    print("Data successfully exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a valid integer.")
        sys.exit(1)

    export_to_json(emp_id)
