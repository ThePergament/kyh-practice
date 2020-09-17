from pathlib import Path
import json

content=Path("uppgift 27.json").read_text(encoding="utf8")
data=json.load=(content)
print(data)

#for ingredient in data:
 #   print(f"{ingredient["what"]})