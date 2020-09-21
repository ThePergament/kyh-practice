import webbrowser
import requests
from pathlib import Path

p= Path ("Uppgift 29.html")
r = requests.get("https://api.adviceslip.com/advice")
advice=r.json()
q_dict =advice ["slip"]
quote =q_dict ["advice"]

template_html =Path ("Uppgift 29.html").read_text()
quote_replace = template_html.replace("QUOTE_TEXT", quote)
print (quote_replace)

new_html=Path("goat_q.html")
new_html.write_text(quote_replace, encoding="utf8")

webbrowser.open("goat_q.html")