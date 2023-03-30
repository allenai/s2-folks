**Next**

**March 28, 2023**

- Our partners (i.e., users of the public Semantic Scholar APIs) have been asking for a higher rate limit for unauthenticated use cases, and we've been listening. We're happy to report that the default rate limit for unauthenticated users is now **5,000 requests per 5 minutes**.
- Our partners have been asking for feature parity between the `/paper/batch` endpoint and the `/paper/{paper_id}` endpoint. We're happy to report that now there is 100% parity between them! As such, you can now get additional paper details (citations, references, and authors) in batch mode by specifying the fields `citations`, `references`, and `authors` when making the POST request. See [documentation](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/post_graph_get_papers) of the `/paper/batch` endpoint for more details.

**March 8, 2023**

- Users of [the academic graph API](https://api.semanticscholar.org/api-docs/graph) can now filter their search results by specifying `publicationTypes`, `venue` and `openAccessPDF` as query parameters when searching for papers. See [documentation](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_get_paper_search) of the `/paper/search` endpoint for more details.
