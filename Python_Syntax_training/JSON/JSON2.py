import json
encodedRetrievedMovie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

film = json.loads(encodedRetrievedMovie,encoding="UTF-8")

with open("sample.json",encoding="UTF-8") as file:
    wynik = json.load(file)

#pprint in load /dump , keys_sort=True / indent =4.
#duolingo.com
#memrsie
