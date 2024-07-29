#!/usr/bin/python3

import requests
import sys

def fetch_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = '{}users/{}'.format(base_url, employee_id)
    todos_url = '{}todos?userId={}'.format(base_url, employee_id)

    user_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    return user, todos

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    user, todos = fetch_data(employee_id)
    
    print("User:", user)
    print("Todos:", todos)

if __name__ == "__main__":
    main()

