
# **August 1, 2023 - August 31, 2023**

### **Breaking Changes**
* **Deprecation of partner.semanticscholar.org**
  * On December 2023 we will turn off access to partner.semanticscholar.org 
  * Ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs before the cutoff date.

### **New Features**
* **Specter2 embeddings**
  * AI2’s SPECTER 2.0 is the latest version of our document embedding models designed specifically for scientific tasks. 
Building upon its predecessor, SPECTER is tailored to generate embeddings for specific tasks, such as Classification, Regression, and Proximity. The API serves pre-computed Proximity embeddings, appropriate for computing the similarity between two documents.  
The model is hosted as [allenai/specter2](https://huggingface.co/allenai/specter2) on HuggingFace, along with the models for other task-specific embeddings.

* **Citations Dataset**
  * Beginning with release “2023-08-29”, a new key, “citationid”, was added to each record.
This is a new, more persistent identifier for citations, which is usable instead of or in addition to the combination of “citingcorpusid” and “citedcorpusid” if desired.

### Performance Improvements
* **API Rate limit reminder**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls

### Other Changes
* **Change in Release Notes Schedule:**
  * We've transitioned from bi-weekly to monthly release notes. Expect updated release notes shortly after the end of each month.
* **Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer




# **June 20, 2023**

- We've launched a new KNN that supports all CS papers in our Recommendations API. Use the 'from' query parameter to specify which pool of papers you want recommendations to pull from. The default value of "recent" pulls papers published within the last 60 days across all fields of study in our corpus. "all-cs" will pull from only CS papers, but covers CS papers across our corpus regardless of publication date. Full documentation [here](https://api.semanticscholar.org/api-docs/recommendations#tag/Paper-Recommendations/operation/get_papers_for_paper)

# **June 6, 2023**

- We’re excited to announce the launch of our Semantic Scholar [API Status Page](https://status.api.semanticscholar.org/). You can find real-time information on system performance and detailed metrics of the API (e.g. response time, error rates), as well as subscribe to updates.

# **April 6, 2023**

- Several API partners have reported that the bulk endpoint `graph/v1/paper/batch` sometimes return papers in an order that's different from the requested paper IDs, and the returned list may be missing some of the requested entries (e.g., https://github.com/allenai/s2-folks/issues/47). We're happy to report that you can now expect the returned list to be of the same size and in the same order as the requested paper IDs.
- Another issue is that various endpoints used to time out when nested authors/papers in the response get too long (e.g., https://github.com/allenai/s2-folks/issues/48), which resulted in mysterious 5XX error codes. We're happy to report that users now get a user friendly error to help them resubmit the requests with a smaller payload.

# **March 28, 2023**

- Our partners (i.e., users of the public Semantic Scholar APIs) have been asking for a higher rate limit for unauthenticated use cases, and we've been listening. We're happy to report that the default rate limit for unauthenticated users is now **5,000 requests per 5 minutes**. Note: this is shared pool among all unauthenticated users. If you are using less than 5,000 requests per 5 minutes and still running into rate limit issues, please submit a request for your own API key [here](https://www.semanticscholar.org/product/api#api-key-form). 
- Our partners have been asking for feature parity between the `/paper/batch` endpoint and the `/paper/{paper_id}` endpoint. We're happy to report that now there is 100% parity between them! As such, you can now get additional paper details (citations, references, and authors) in batch mode by specifying the fields `citations`, `references`, and `authors` when making the POST request. See [documentation](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/post_graph_get_papers) of the `/paper/batch` endpoint for more details.

# **March 8, 2023**

- Users of [the academic graph API](https://api.semanticscholar.org/api-docs/graph) can now filter their search results by specifying `publicationTypes`, `venue` and `openAccessPDF` as query parameters when searching for papers. See [documentation](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_get_paper_search) of the `/paper/search` endpoint for more details.
