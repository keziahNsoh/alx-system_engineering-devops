#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a specific employee
from the JSONPlaceholder API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress for a given employee ID.
    
    Args:
        employee_id (int): The ID of the employee whose TODO progress is to be fetched.
    """
    # Define the API endpoints
    api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)

    try:
        # Fetch employee details
        with urllib.request.urlopen(api_url) as response:
            employee_data = json.loads(response.read().decode())
            employee_name = employee_data.get('name', 'Unknown')

    except urllib.error.HTTPError as e:
        print("Error fetching employee details: {}".format(e))
        return

    # Fetch TODO list for the employee
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    try:
        with urllib.request.urlopen(todo_url) as response:
            todos = json.loads(response.read().decode())

    except urllib.error.HTTPError as e:
        print("Error fetching TODO list: {}".format(e))
        return

    # Calculate completed and total tasks
    total_tasks = len(todos)
    completed_tasks = [todo.get('title') for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    # Print the result
    print('Employee {} is done with tasks({}/{})'.format(
        employee_name, number_of_done_tasks, total_tasks))
    
    for task in completed_tasks:
        print('\t {}'.format(task))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter a valid integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

