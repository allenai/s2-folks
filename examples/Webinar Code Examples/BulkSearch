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

# Define the search query and filters
query = "covid vaccination"
fields = "paperId,title,year,authors,fieldsOfStudy"
limit = 1000  # Fetch up to 1000 papers in one request
publication_types = "JournalArticle,Review"  # Filter by publication types
fields_of_study = "Medicine,Public Health"  # Filter by fields of study
year = "2020-2023"  # Papers published between 2020 and 2023

response = http.get(
    "https://api.semanticscholar.org/graph/v1/paper/search/bulk",
    headers={'x-api-key': API_KEY},
    params={
        'query': query,
        'fields': fields,
        'limit': limit,
        'publicationTypes': publication_types,
        'fieldsOfStudy': fields_of_study,
        'year': year
    }
)

response.raise_for_status()  # Ensures we stop if there's an error
data = response.json()

# Output the fetched data
print(f"Total estimated matches: {data.get('total')}")
for paper in data.get('data', []):
    print(f"Paper ID: {paper.get('paperId')}")
    print(f"Title: {paper.get('title')}")
    print(f"Year: {paper.get('year')}")
    print("Authors:", ', '.join([author['name'] for author in paper.get('authors', [])]))
    print("Fields of Study:", ', '.join(paper.get('fieldsOfStudy', [])))
    print("---")

# Handle continuation token if there are more results to fetch
if 'token' in data:
    print(f"Continuation Token: {data['token']}")
