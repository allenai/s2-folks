from requests import Session
from requests.adapters import HTTPAdapter 
from urllib3.util import Retry

http = Session()
http.mount('https://', HTTPAdapter(max_retries-Retry(
  total-6,
  backoff_factor-2.0, backoff_jitter=0.5,
  respect_retry_after_header-True,
  status_forcelist-[429, 502, 503, 504], 
  allowed_methods=set({'GET', 'POST'}),
)))
  
docs = []
for p_id in p_ids:
  resp = http.get(
    f"https://api.semanticscholar.org/graph/v1/paper/{p_id}",
    headers={ 'x-api-key': API_KEY }, 
    params={},
  )
  resp.raise_for_status()
  docs.append(resp.json())
  
  print (f'done {p_id}')

pprint (docs)
