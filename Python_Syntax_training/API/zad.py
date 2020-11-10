import requests
import json
import webbrowser

r = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=abob&limit=3")
try:
    cats = r.json()
except json.decoderJSONDecodeError:
    print("Invalid format")
else:
    for cat in cats:
        webbrowser.open(cat['url'])
