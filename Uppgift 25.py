#Nu ska vi bearbeta datan något med hjälp av Python och f-string tricken jag visade er!
#25.1 Skriv ett Pythonprogram som skriver ut framtida kurstillfällen, på denna form:
#Kursnamn:      Professional Scrum Product Owner (EN), 15-16 september, Stockholm
#Startdatum:    2020-09-15
#Slutdatum:     2020-09-17
#Kursnamn:      Professional Scrum Master, 15-16 september, Stockholm
#Startdatum:    2020-09-15
#Slutdatum:     2020-09-16
#Osv.
#Det går bra att "hårdkoda" dagens datum: 2020-09-15, och använda som filter på startDate (det går att använda mindre än och större än tecken för att jämföra datumsträngar som är formatterade enligt YYYY-MM-DD, mycket bra egenskap med det formatet!!)
#25.2 Istället för att hårdkoda dagens datum, använd denna funktion:
 #   today = datetime.datetime.today()
#"today" blir ett objekt med attribut som .year, .month och .day. Bygg ihop dagens datum dynamiskt (d.v.s när programmet
#kör)!







import requests
import json
from pprint import pprint

r=requests.get('https://proagile.se/api/publicEvents')
data=json.loads(r.text)
#pprint (data)
namn= "Kursnamn:"
startdatum= "Startdatum:"
slutdatum="Slutdatum"

for i in data:
    if "name" in i:
        print(f"{namn}", i["name"])
    if "startDate" in i:
        print(f"{startdatum}", i["startDate"])
            #(i(f"{startdatum}", int["startDate"]))
    if "endDate" in i:
        print(f"{slutdatum}", i["endDate"], "\n")
