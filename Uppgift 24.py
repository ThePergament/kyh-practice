import requests
import json
from pprint import pprint

r=requests.get('https://proagile.se/api/publicEvents')
data=json.loads(r.text)
pprint (data)