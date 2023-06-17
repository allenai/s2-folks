import requests
import urllib
import os

# Get info about the latest release
latest_release = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest").json()
print(latest_release['README'])
print(latest_release['release_id'])

# Get info about past releases
dataset_ids = requests.get("http://api.semanticscholar.org/datasets/v1/release").json()
earliest_release = requests.get(f"http://api.semanticscholar.org/datasets/v1/release/{dataset_ids[0]}").json()

# Print names of datasets in the release
print("\n".join(d['name'] for d in latest_release['datasets']))

# Print README for one of the datasets
print(latest_release['datasets'][2]['README'])

# Get info about the papers dataset
papers = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/papers",
                      headers={'X-API-KEY':os.getenv("S2_API_KEY")}).json()

# Download the first part of the dataset
urllib.request.urlretrieve(papers['files'][0], "papers-part0.jsonl.gz")
