import requests
import json

query = "sturgeon"
fields = "title,year"

url = f"http://api-dev.semanticscholar.org/graph/v1/paper/search/bulk?query={query}&fields={fields}"
r = requests.get(url).json()

print(f"Will retrieve {r['total']} documents")
retrieved = 0

with open(f"{query}.jsonl", "a") as file:
    while True:
        for paper in r["data"]:
            print(json.dumps(paper), file=file)
        token = r["token"]
        if token:
            retrieved += len(r["data"])
            print(f"Retrieved {retrieved} papers...")
        else:
            break
        r = requests.get(f"{url}&token={token}").json()
print("Done!")
