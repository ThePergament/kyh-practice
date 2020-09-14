from pathlib import Path
import json
def main():
    content=Path("massasdata.json").read_text(encoding="utf8")
    data=json.loads(content)
    print(data)
    totaltotal=0
    for i in data["entries"]:
        totaltotal+=i["total"]
    print(totaltotal)







if __name__ == "__main__":
    main()
