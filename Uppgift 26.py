
import requests
import json
import datetime
from pprint import pprint

r=requests.get('http://www.omdbapi.com/',params = {"t": "Alien", "apikey": "9f6d550c"})

data=r.json() #loads(r.text)
pprint (data)



