import requests
import json
import credentials

def get_json_content_from_responce(responce):
    try:
        content = responce.json()
    except json.decoderJSONDecodeError:
        print("Invalid Format",responce.text)
    else:
        return content

def get_favourite_cats(userId):
    params = {
        "sub_id": userId
        }
    r = requests.get("https://api.thecatapi.com/v1/favourites/",params,headers = credentials.headers)
    return get_json_content_from_responce(r)

def get_random_cat():
     r = requests.get("https://api.thecatapi.com/v1/images/search",headers = credentials.headers)
     return get_json_content_from_responce(r)

def add_favourite_cat(catId,userId):
    catData = {
        "image_id":catId,
        "sub_id":userId
        }
    r = requests.post("https://api.thecatapi.com/v1/favourites/", json = catData,headers = credentials.headers)
    return get_json_content_from_responce(r)

def remove_favourite_cat(idCatToRemove):
    r = requests.delete("https://api.thecatapi.com/v1/favourites/" + idCatToRemove,headers = credentials.headers)
    return get_json_content_from_responce(r)
#menu
print("Hej zaloguj sie - podaj login i haslo")

name = "Arkadiusz"
userId = "dupa"

print("Witaj " + name)
favourite_cats = get_favourite_cats(userId)
print("Twoje ulubione kotki: ", favourite_cats)
randomCat = get_random_cat()
print("wylosowano kotka: ", randomCat[0]["url"])

addToFavourites = input("Czy chcesz go dodac do ulubionych?")

if(addToFavourites == "T"):
    print(add_favourite_cat(randomCat[0]["id"],userId))
else:
    print("Kotek jest smutny")

favouriteCatById = {
    favouriteCat["id"]: favouriteCat["image"]["url"]
    for  favouriteCat in favourite_cats 
}

idCatToRemove = input("Zajeb kota, podaj Id ofiary")    
print(remove_favourite_cat(idCatToRemove))
