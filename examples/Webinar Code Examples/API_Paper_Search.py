import requests
import json
import os

# Fetch API key from environment variables
api_key = os.getenv("S2_API_KEY")
if not api_key:
    raise EnvironmentError("S2_API_KEY environment variable not set.")

# Set up the headers with the API key
headers = {
    "x-api-key": api_key
}

# Set the fields as a query parameter
params = {
    "fields": "referenceCount,citationCount,title"
}

# Make the POST request with headers and params
r = requests.post(
    'https://api.semanticscholar.org/graph/v1/paper/batch',
    headers=headers,
    params=params,
    json={
        "ids": ["649def34f8be52c8b66281af98ae884c09aef38b", "ARXIV:2106.15928"]
    }
)

# Check if the request was successful
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2))
else:
    print(f"Error: {r.status_code}")
    print(json.dumps(r.json(), indent=2))
