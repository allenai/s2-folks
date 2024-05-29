import os
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Fetch the API key from environment variables
API_KEY = os.getenv('S2_API_KEY')

if not API_KEY:
    raise ValueError("API key not found in environment variables.")

http = Session()
http.mount('https://', HTTPAdapter(max_retries=Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods={"HEAD", "GET", "OPTIONS"}
)))

# Define the search query and the fields you want to retrieve
query = "covid vaccination"
fields = "paperId,title,url,abstract,authors"
limit = 3  # Limit the number of results to 3
offset = 100  # Start returning results from this offset

response = http.get(
    "https://api.semanticscholar.org/graph/v1/paper/search",
    headers={'x-api-key': API_KEY},
    params={'query': query, 'fields': fields, 'limit': limit, 'offset': offset}
)

response.raise_for_status()  # Ensures we stop if there's an error
data = response.json()

# Output the fetched data
for paper in data.get('data', []):
    print(f"Paper ID: {paper.get('paperId')}")
    print(f"Title: {paper.get('title')}")
    print(f"URL: {paper.get('url')}")
    print("Authors:", ', '.join([author['name'] for author in paper.get('authors', [])]))
    print(f"Abstract: {paper.get('abstract')}\n")

print(f"Total results: {data.get('total')}")
print(f"Next offset: {data.get('next')}")
