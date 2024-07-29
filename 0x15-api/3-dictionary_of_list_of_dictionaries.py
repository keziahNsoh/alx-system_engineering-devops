#!/usr/bin/python3

import json
import requests
import sys

def fetch_all_data():
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = '{}users'.format(base_url)
    todos_url = '{}todos'.format(base_url)
    
    try:
        # Fetch all users
        users_response = requests.get(users_url)
        users_response.raise_for_status()
        users_data = users_response.json()
        
        # Fetch all todos
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        return users_data, todos_data
    except requests.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)

def export_to_json(users_data, todos_data):
    filename = 'todo_all_employees.json'
    
    # Create a dictionary where each key is a user ID and value is a list of todos
    todo_dict = {}
    
    for user in users_data:
        user_id = user['id']
        user_todos = [todo for todo in todos_data if todo['userId'] == user_id]
        todo_dict[user_id] = user_todos
    
    with open(filename, 'w') as file:
        json.dump(todo_dict, file, indent=4)
    
    print("Data exported to {}".format(filename))

def main():
    users_data, todos_data = fetch_all_data()
    export_to_json(users_data, todos_data)

if __name__ == "__main__":
    main()

