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

# Specify the author_id and the fields you want to fetch
author_id = "1741101"
fields = "authorId,name,papers.paperId,papers.title,papers.abstract,papers.authors"

# Make the GET request to fetch author details with the specified fields
r = requests.get(
    f'https://api.semanticscholar.org/graph/v1/author/{author_id}',
    headers=headers,
    params={'fields': fields}
)

# Check if the request was successful
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2))
else:
    print(f"Error: {r.status_code}")
    if r.text:
        print(json.dumps(r.json(), indent=2))
    else:
        print("No additional error information is provided.")

