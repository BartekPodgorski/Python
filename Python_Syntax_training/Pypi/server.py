"""
JSONplaceholder
"""

import requests
#import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)

def count_task_freuency(tasks):
    completed_task_frequency_by_user = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completed_task_frequency_by_user[entry["userId"]] += 1
            except KeyError:
                completed_task_frequency_by_user[entry["userId"]] = 1
    return completed_task_frequency_by_user

def users_top(completed_task_frequency_by_user):
    number_task_max_user_id = []
    for userId,number_task in completed_task_frequency_by_user.items():
        if(number_task == max(completed_task_frequency_by_user)):
           number_task_max_user_id.append(userId)
    return number_task_max_user_id

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format ")
else:

    completed_task_frequency_by_user = count_task_freuency(tasks)
    print(users_top(completed_task_frequency_by_user))
  
    
