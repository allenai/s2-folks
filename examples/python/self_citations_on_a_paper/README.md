For some paper, identifies citations and references with other papers that share at least one author.

Example

* Paper 1 authors: A, B. Paper 1 cites paper 2.
* Paper 2 authors: B, C. Paper 2 cites paper 3.
* Paper 3 authors: C, D

Looking at paper 2, author B self-cites because they are an author on paper 1 which cites paper 2.
Also looking at paper 2, author C self-cites because they are an author on paper 2 which cites paper 3.

In this context, a *citation* is another paper that cited the paper of interest, 
and a *reference* is another paper that the paper of interest cited.

APIs involved
* [/graph/v1/paper/{paper_id}](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/get_graph_get_paper)
* [/graph/v1/paper/{paper_id}/citations](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/get_graph_get_paper_citations)
* [/graph/v1/paper/{paper_id}/references](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/get_graph_get_paper_references)

Note that you can follow some of a paper's citations/references using the first API endpoint
using a request like
https://api.semanticscholar.org/graph/v1/paper/CorpusID:3658586?fields=references.authors,citations.authors
but only up to 500 elements in nested collections will be returned. 
Use the specialized API endpoints for to page through all citations/references. e.g.
https://api.semanticscholar.org/graph/v1/paper/CorpusID:3658586/citations?fields=authors&limit=1000&offset=0
https://api.semanticscholar.org/graph/v1/paper/CorpusID:3658586/references?fields=authors&limit=1000&offset=0

