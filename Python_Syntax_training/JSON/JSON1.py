"""

JSON - wspolny zapis danych
json.dumps(data)- zapiseuj dane do postaci stringowej json
json.dump(data,nameOfFile,ensure_ascii=False) zapisuje dane
do pliku w postaci json
"""
import json 

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encoded_film = json.dumps(film, ensure_ascii=False)
with open("sample.json","w",encoding = "UTF-8") as file:
    json.dump(film,file,ensure_ascii=False)

"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""

