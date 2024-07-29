#!/usr/bin/python3
"""
This script exports the TODO list of a specific employee to a CSV file.

Usage:
    python3 1-export_to_CSV.py <employee_id>
"""

import csv
import json
import sys
import urllib.request


def fetch_employee_data(employee_id):
    """
    Fetches employee data from the API.

Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: Employee data.
    """
    api_url = (
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    )

    try:
        with urllib.request.urlopen(api_url) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error fetching employee details: {}".format(e))
        sys.exit(1)


def fetch_todo_data(employee_id):
    """
    Fetches TODO list data for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of TODO items.
    """
    todo_url = (
        'https://jsonplaceholder.typicode.com/users/'
        '{}/todos'.format(employee_id)
    )

    try:
        with urllib.request.urlopen(todo_url) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error fetching TODO list: {}".format(e))
        sys.exit(1)


def export_to_csv(employee_id, username, todos):
    """
    Exports TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        username (str): The username of the employee.
        todos (list): List of TODO items.
    """
    filename = '{}.csv'.format(employee_id)

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get('completed'),
                todo.get('title')
            ])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a valid integer.")
        sys.exit(1)

    # Fetch employee data
    employee_data = fetch_employee_data(employee_id)
    username = employee_data.get('username', 'Unknown')

    # Fetch TODO list
    todos = fetch_todo_data(employee_id)

    # Export data to CSV
    export_to_csv(employee_id, username, todos)
