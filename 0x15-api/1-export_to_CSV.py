#!/usr/bin/python3

import requests
import csv
import sys

def fetch_data(user_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    todos_url = '{}todos?userId={}'.format(base_url, user_id)
    response = requests.get(todos_url)
    return response.json()

def export_to_csv(user_id):
    todos = fetch_data(user_id)
    filename = '{}_todos.csv'.format(user_id)
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'ID', 'TITLE', 'COMPLETED']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': todo['userId'],
                'ID': todo['id'],
                'TITLE': todo['title'],
                'COMPLETED': todo['completed']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    export_to_csv(user_id)

