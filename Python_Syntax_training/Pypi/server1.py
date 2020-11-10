#ciacho dla Boga

import requests
import json
from collections import defaultdict
"""
1:11
2:6
3:15
"""

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTasksFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if(entry["completed"] == True):
            completedTasksFrequencyByUser[entry["userId"]] += 1
                          
    return completedTasksFrequencyByUser


"""
# funkcja zwracajaca klucze najwyzszych wartosci w moim slowniku (uniwersalna)
def get_keys_with_top(my_dict):
     return [
        key
        for (key,value) in my_dict.items()
        if value == max(my_dict.values())
    ]
"""
def find_maximum(completedTasksFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTasksFrequencyByUser.values())
    for userId,numberOfCompletedTask in completedTasksFrequencyByUser.items():
        if(numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
            
    return usersIdWithMaxCompletedAmountOfTasks

try:
    tasks = r.json()
except json.decoderJSONDecodeError:
    print("Invalid Format")
else:
    completedTasksFrequencyByUser = count_task_frequency(tasks)
    userWithTopCompletedTasks = find_maximum(completedTasksFrequencyByUser)
#sposob 1
    """
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

for user in users:
    if(user["id"] in userWithTopCompletedTasks):
        print("Ciasteczko mistrza goes to:",user["name"])

#sposob 2
for userId in  userWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/"+ str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    print("Ciasteczko mistrza goes to:",user[0]["name"])

#sposob 3

def change_list_into_conj_of_param(my_list, key = "id"):
    conj_param = key + "="
    lastIterationNumber = len(my_list)
    i = 0
    for item in my_list:
        i +=i
        if (i == lastIterationNumber):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
    
    return conj_param
    
conjm_param = change_list_into_conj_of_param(userWithTopCompletedTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users", params=conjm_param)
users = r.json()
for user in users:
    print("Ciasteczko mistrza goes to:",user["name"])
"""
        

