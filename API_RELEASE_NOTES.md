# **RELEASE NOTES DISCONTINUED**

# **November 2024**
### Breaking change:
*  API keys found to be inactive for ~60 days will be automatically pruned.
*  New key applications and past key recovery are backlogged by about 1 month.


# **October 2024**
### Breaking change:
*  API keys found to be inactive for ~60 days will be automatically pruned.
*  New key applications and past key recovery are backlogged by about 1 month.


### Ongoing Reminders:
  *  We no longer accept key requests from free email domains due to limited resources. 
  *  We no longer approve key requests for 3rd party apps.
  *  Due to the requirements of our agreement with Springer, abstracts are not available via API.
  *  We now require the use of exponential backoff strategies for API requests.
    
# **September 2024**
### Ongoing Reminders:
  *  We no longer accept key requests from free email domains due to limited resources. 
  *  We no longer approve key requests for 3rd party apps.
  *  Due to the requirements of our agreement with Springer, abstracts are not available via API.
  *  We now require the use of exponential backoff strategies for API requests.
    
# **August 2024**
### **Breaking Changes**
  * We can no longer approve key requests from free email domains due to limited resources. This will not impact you if you already have a key. We appreciate your understanding.
  * We can no longer approve key requests for 3rd party apps. We are working with 3rd party developers to incorporate our data into their applications wherever possible.
    
### Ongoing Reminders:
  *  Springer abstracts: Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to the requirements of our agreement with Springer.
  *  Using multiple keys: If you need multiple keys, please contact feedback@semanticscholar.org to coordinate with us to prevent service disruptions.
  *  Exponential backoff required: To enhance system stability and manage the load effectively, we now require the use of exponential backoff strategies for API requests.

    
# **July 2024**
### **Breaking Changes**
  * No breaking changes
    
### Ongoing Reminders:
  *  Springer abstracts: Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to the requirements of our agreement with Springer.
  *  Using multiple keys: If you need multiple keys, please contact feedback@semanticscholar.org to coordinate with us to prevent service disruptions.
  *  Exponential backoff required: To enhance system stability and manage the load effectively, we now require the use of exponential backoff strategies for API requests.
 
# **June 2024**
### **Breaking Changes**
  * No breaking changes
    
### **New Feature**
  * Title Search: Returns a single paper with the closest title match. https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/get_graph_paper_title_search

### Performance Improvements:
  * Improved monitoring: Our service status page https://status.api.semanticscholar.org/ is now reporting metrics as P90. We expect this change to improve user experience when our systems are experiencing heavy load.
  * Datasets cleanup: TLDR and Abstracts contained some duplicate data. This has been resolved. Note that incremental updates will not remove the duplicates. If you are impacted, please re-download the entire latest dataset to replace it with a deduplicated copy from any release of '2024-06-18' or later.

### Ongoing Reminders:
  *  Springer abstracts: Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to the requirements of our agreement with Springer.
  *  Using multiple keys: If you need multiple keys, please contact feedback@semanticscholar.org to coordinate with us to prevent service disruptions.
  *  Exponential backoff required: To enhance system stability and manage the load effectively, we now require the use of exponential backoff strategies for API requests.
 
# **May 2024**
### **Breaking Changes**
  * As announced a while ago, we've successfully deprecated the 'aliases' field! This change prevents instances of deadnaming and ensures we're respecting the identities of individuals in our database.

### Performance Improvements:
  * Rate Plan redesign: All new key requests receive a 1 RPS rate limit on all endpoints.
  * Unauthenticated pool reduction:  We are observing the results of reducing rate limits. Based on our findings, we may introduce further reductions in the following months.

### Ongoing Reminders:
  *  Springer abstracts: Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to the requirements of our agreement with Springer.
  *  Using multiple keys: If you need multple keys please contact feedback@semanticscholar.org to coordinate with us to prevente service disruptions
  *  Exponential backoff required: To enhance system stability and manage the load effectively, we now require the use of exponential backoff strategies for API requests.

# **April 2024**
### Performance Improvements:
  * Rate Plan redesign: All new key requests receive a 1 RPS rate limit on all endpoints.
  * Unauthenticated pool reduction:  We are observing the results of reducing rate limits. Based on our findings, we may introduce further reductions in the following months.

### Ongoing Reminders:
  *  Springer abstracts: Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to the requirements of our agreement with Springer.
  *  Using multiple keys: If you are using multiple keys in your application, please contact us via christopherf@allenai.org so that we can understand your use case and ensure service stability. You may experience service disruptions using multiple keys if we aren't aware of your use case.
  *  Exponential backoff required: To enhance system stability and manage the load effectively, we now require the use of exponential backoff strategies for API requests.


* # **March 2024**
### **Breaking Changes**
* **partner.semanticscholar.org has been deprecated**
  * Please ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs. 

### Performance Improvements
* **Rate Plan redesign**
  * We found that our highest limit rate plan is never utilized, and recognized this as a risk to accidental outages from legacy keys which were given this limit while we had 10x fewer users. This rate plan with few exceptions will be deprecated. If you're concerned, please reach out and please rest assured we are performing analytics on each user to prevent unintended disruptions
  * More to come on redesigning rate plans to better fit usage profiles in the coming months.

* **Unauthenticated pool reduction**
  * With increased traffic and renewed emphasis on systems observability, we are reducing global rate limits on the unauthenticated request pool. 

* **Exponential backoff required**
  * To enhance system stability and manage the load effectively, we now require the use of exponential backoff strategies for API requests. When a request fails, particularly due to rate limiting, implementing an exponential backoff involves systematically increasing the delay before retrying the request. This approach helps prevent overloading our systems and ensures a smoother experience for all users. Please integrate exponential backoff into your retry mechanisms to comply with our updated rate plan and performance improvements.

### Other Changes
* **TOS regarding multiple keys**
  * Please note: We provide a key to each person or project with our best effort to manage rate limits and the number of keys. Some users have been using multiple keys as a solution for needing higher rate limits that we can support. If you are doing this, please reach out to me at christopherf@allenai.org so that we can find an alternative solution. 

* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to the requirements of our agreement with Springer.

# **February 2024**

### **Breaking Changes**
* **Field Deprecation - Aliases**
  * Date of change is TBD 

* **Ongoing Reminder: Deprecation of partner.semanticscholar.org**
  * This was planned for December 2023 but is now being reprioritized. 
  * Please ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs as we are still planned to discontinue supporting the partner* domain. 

### Performance Improvements
* **Ongoing Reminder API Rate limit**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * - We are in making refinements to the implementation of the unauthenticated request group. Please be aware that in 2024 we hope to increase usage of authenticated requests with the intent to move users away from making unauthenticated requests whenever possible.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls


### Other Changes
* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer


# **Janurary 2024**

### **Breaking Changes**
* **Field Deprecation - Aliases**
  * Date of change is TBD 

* **Ongoing Reminder: Deprecation of partner.semanticscholar.org**
  * This was planned for December 2023 but is now being reprioritized. 
  * Please ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs as we are still planned to discontinue supporting the partner* domain. 

### Performance Improvements
* **Ongoing Reminder API Rate limit**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls

### Other Changes
* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer

# **December 2023**

### **Breaking Changes**
* **Field Deprecation - Aliases**
  * Date of change is reverted to TBD 

* **Ongoing Reminder: Deprecation of partner.semanticscholar.org**
  * This was planned for December 2023 but is now anticipated to take place by end of January 2024
  * Ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs before the cutoff date.

### Performance Improvements
* **Ongoing Reminder API Rate limit**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls

### Other Changes
* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer

# **November 2023**

### **Breaking Changes**
* **Field Deprecation - Aliases**
  * Starting in January of next year we will not longer support the Aliases field.

* **Ongoing Reminder: Deprecation of partner.semanticscholar.org**
  * In December 2023 we will turn off access to partner.semanticscholar.org 
  * Ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs before the cutoff date.

### **New Features**
* **New Field: contextsWithIntent**
  * Similar to "contexts" but each context comes with its associated intents. Each object returned in this list has two keys: 'context' - the text snippet, and 'intents' - associated intents for this context. For example 
                    '{
                        "context": "SciBERT (Beltagy et al., 2019) follows the BERT’s ...",
                        "intent": "methodology", }'

### Performance Improvements
* **Ongoing Reminder API Rate limit**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls

### Other Changes
* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer


# **October 2023**

### **Breaking Changes**
* **Field Deprecation - Aliases**
  * In our commitment to inclusivity and respecting user identities, starting January 2024, we will no longer support the Aliases field to prevent instances of deadnaming.

* **Reduction of Relevance Search maximum results from 10,000 to 1,000**
  * As planned, on October 31st we reduced the maximum sum of offset and limit from 10,000 to 1,000 results.
  * For needs which exceed this limitation please utilize either our [open corpus via the Datasets API](https://api.semanticscholar.org/api-docs/datasets) or our [Paper Bulk Search via the Academic Graph API](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_paper_bulk_search)

* **Ongoing Reminder: Deprecation of partner.semanticscholar.org**
  * In December 2023 we will turn off access to partner.semanticscholar.org 
  * Ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs before the cutoff date.


### **New Features**
* **No new features for this release update**


### Performance Improvements
* **Ongoing Reminder API Rate limit**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls


### Other Changes
* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer
 


# **September 2023**

### **Breaking Changes**
* **Updated Terms of Service**
  * We updated our terms of service on May 17, 2023.
  * In order to comply with legal we will be turning off API keys which have not accepted our updated terms of service by Monday October 16, 2023
  * Please review and accept the updated agreement [here](https://www.semanticscholar.org/product/api/license)

* **Reduction of Relevance Search maximum results from 10,000 to 1,000**
  * On October 31st we reduce the maximum sum of offset and limit from 10,000 to 1,000 results.
  * For needs which exceed this limitation please utilize either our [open corpus via the Datasets API](https://api.semanticscholar.org/api-docs/datasets) or our [Paper Bulk Search via the Academic Graph API](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_paper_bulk_search)

* **Ongoing Reminder: Deprecation of partner.semanticscholar.org**
  * In December 2023 we will turn off access to partner.semanticscholar.org 
  * Ensure that you replace "partner.semanticscholar.org" with "api.semanticscholar.org" in all URLs before the cutoff date.


### **New Features**
* **Incremental Datasets**
  * This feature allows you to update your datasets by downloading only the changes made since your last download. Benefits: Update datasets without downloading everything from scratch and save on download time and storage.
  * [Relevant API Documentation ](https://api.semanticscholar.org/api-docs/datasets#tag/Incremental-Updates)
  * [Github code sample](https://github.com/allenai/s2-folks/blob/main/examples/python/s2ag_datasets/incremental-updates.py)

* **Paper Bulk Search**
  * This feature is perfect for matching and filtering our paper data down to small sub-corpora. Our relevance search was limited in size, and our full corpus downloads involved sifting through many unrelated entries. Paper Bulk Search fits the use-case right in between!
  * Benefits: Targeted Data Downloads: Isolate and download small sub-corpora of paper data. Allows matching and fetching up to 10,000,000 papers in batches of 1000 - far more than our relevance search method. Utilizes an optional simple boolean query against paper titles and abstracts. Results can be sorted by date, citation count, or Paper ID. Page size is fixed for efficiency.
  * [Relevant API Documentation](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_paper_bulk_search)
  * [Github code sample](https://github.com/allenai/s2-folks/tree/main/examples/python/search_bulk)

* **New Filtering and Sorting in Paper Relevance and Paper Bulk search**
  * Both search methods now support filtering on publicationDateOrYear and minCitationCount and the bulk search method now allows sorting the results by publicationDate or citationCount


### Performance Improvements
* **Ongoing Reminder API Rate limit**
  * Unauthenticated: All unauthenticated users share a limit of 5,000 requests per 5 minutes.
  * Authenticated: 1 request per second for: /paper/batch, /paper/search, /recommendations and 10 requests / second for all other calls


### Other Changes
* **Ongoing Reminder: Springer abstracts**
  * Users have commented that our Public API does not show an abstract for Springer papers. This is intentional due to requirements of our agreement with Springer




# **August 2023**

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
