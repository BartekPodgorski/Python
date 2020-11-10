import requests
import json
import webbrowser

params = {
    "amount":5,
    "animal_type":"cat"
    }

print("Welcome in my program!")
wybor = int(input(""""If uou want to see some facts about dogs click 1,
If you want to see some facts about cats click 2: """))

if (wybor == 1):
    params["animal_type"] = "dog"
    print(params)
    d = requests.get("https://cat-fact.herokuapp.com/facts/random",params)
    try:
        content = d.json()
    except json.decoder.JSONEncodeError:
        print("Invalid format")
    else:
        for dog in content:
            print(dog["text"])
if (wybor == 2):
    params["animal_type"] = "cat"
    print(params)
    c = requests.get("https://cat-fact.herokuapp.com/facts/random",params)
    try:
        content = c.json()
    except json.decoder.JSONEncodeError:
        print("Invalid format")
    else:
        for cat in content:
            print(cat["text"])    
