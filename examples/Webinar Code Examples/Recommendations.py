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

# Define the payload with positive and negative paper IDs
payload = {
    "positivePaperIds": ["649def34f8be52c8b66281af98ae884c09aef38b"],
    "negativePaperIds": ["ArXiv:1805.02262"]
}

# Specify the fields you want to fetch for each recommended paper
fields = "paperId,title,authors"

# Define the limit for the number of recommendations to return
limit = 100

# Make the POST request to get paper recommendations
response = requests.post(
    'https://api.semanticscholar.org/recommendations/v1/papers/',
    headers=headers,
    json=payload,
    params={'fields': fields, 'limit': limit}
)

# Check if the request was successful
if response.status_code == 200:
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    # It's better to print response.text for non-200 responses, as they may not be in JSON format
    print(response.text)

