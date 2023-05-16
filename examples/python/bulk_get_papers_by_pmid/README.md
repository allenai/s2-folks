S2 APIs involved:
* [POST /graph/v1/paper/batch](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/post_graph_get_papers)

This example fetches paper data from a list of PMIDs [pmid-p53-set.txt] retrieved from

https://pubmed.ncbi.nlm.nih.gov/?term=p53&filter=pubt.clinicaltrial&filter=pubt.review&filter=years.2020-2020&size=200

and maps JSON returned by the semanticscholar API into papers.csv

To run

    python get_papers.py


[pmid-p53-set.txt]: ./pmid-p53-set.txt