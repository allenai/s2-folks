"""
Sample usage of Semantic Scholar Academic Graph Datasets API
https://api.semanticscholar.org/api-docs/datasets
"""
import requests
import urllib
import json
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
papers = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/papers",headers={'x-api-key':os.getenv("S2_API_KEY")}).json()

# Download the dataset
urllib.request.urlretrieve(papers['files'][0], "papers-part0.jsonl.gz")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Explore datasets
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Papers
papers = [json.loads(l) for l in open("papers/papers-sample.jsonl","r").readlines()]

## Citations
citations = [json.loads(l) for l in open("citations/citations-sample.jsonl","r").readlines()]

## Embeddings
embeddings = [json.loads(l) for l in open("embeddings/embeddings-sample.jsonl","r").readlines()]

## S2ORC
docs = [json.loads(l) for l in open("s2orc/s2orc-sample.jsonl","r").readlines()]
text = docs[0]['content']['text']
annotations = {k:json.loads(v) for k,v in docs[0]['content']['annotations'].items() if v}

for a in annotations['paragraph'][:10]: print(a)
for a in annotations['bibref'][:10]: print(a)
for a in annotations['bibentry'][:10]: print(a)

def text_of(type):
  return [text[a['start']:a['end']] for a in annotations[type]]

text_of('abstract')

print('\n\n'.join(text_of('paragraph')[:3]))

print('\n'.join(text_of('bibref')[:10]))
