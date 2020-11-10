import requests
import json
from pprint import pprint

params ={
    "api_key":"a1043a03eb80f579db9d1197806ae2307a79925a",
    "country":"pl",
    "year":2020
}

r = requests.get("https://calendarific.com/api/v2/holidays/", params)

try:
    web = r.json()
except json.decoderJSONDecodeError:
    print("Invalid Format")
else:
    pprint(web)
