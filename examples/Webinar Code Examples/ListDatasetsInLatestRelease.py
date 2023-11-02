import requests
import json

# Fetch the ID of the latest release
response_latest_release = requests.get('https://api.semanticscholar.org/datasets/v1/release/latest')
latest_release_id = response_latest_release.json()['release_id']
print(f"Latest Release ID: {latest_release_id}")
# Fetch the datasets available in the latest release
response_datasets = requests.get(f'https://api.semanticscholar.org/datasets/v1/release/{latest_release_id}')
datasets = response_datasets.json()['datasets']

# Print available datasets
print("\nAvailable datasets in the latest release:")
for dataset in datasets:
    print(f"- Name: {dataset['name']}\n  Description: {dataset['description']}\n")

