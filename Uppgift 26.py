
import requests
import json
from pprint import pprint

movie=input("Ange film:")
r=requests.get('http://www.omdbapi.com/',params = {"t": movie, "apikey": "9f6d550c"})
text=r.text
result=json.loads(text)

pprint('*** Resultat från OMDB! ***')
titel=result["Title"]
year=result["Year"]
director=result["Director"]
actors=result["Actors"]
rating=result ["imdbRating"]
awards=result["Awards"]
runtime=result["Runtime"]
print(f"Titel:{titel} ({year}) regisserades av {director}\n "
      f"Skådisar: {actors}\n"
      f"IMDB betyg: {rating}\n"
      f"Kaka:{awards}\n"
      f"   Längd:{runtime}")







