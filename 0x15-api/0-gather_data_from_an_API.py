#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress of an employee
from a REST API based on a given employee ID.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of a given employee.
    Args:
        employee_id (int): The ID of the employee.
    """
    # Define the API endpoints
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    # Fetch employee data
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise HTTPError for bad responses
        user_data = user_response.json()
    except requests.RequestException as e:
        print('Error fetching user data: {}'.format(e))
        sys.exit(1)

    # Fetch TODO data
    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()  # Raise HTTPError for bad responses
        todos_data = todos_response.json()
    except requests.RequestException as e:
        print('Error fetching TODO data: {}'.format(e))
        sys.exit(1)

    # Extract employee name and TODO list
    employee_name = user_data.get('name', 'Unknown')
    total_tasks = len(todos_data)
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Print the results
    print('Employee {} is done with tasks({}/{}):'.format(employee_name, number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print('    {}'.format(task))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print('Invalid employee ID. Please enter a valid integer.')
        sys.exit(1)

    get_employee_todo_progress(emp_id)
