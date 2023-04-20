This example fetches paper data from a list of PMIDs retrieved from

https://pubmed.ncbi.nlm.nih.gov/?term=p53&filter=datesearch.y_1&size=10

and maps JSON returned by the semanticscholar API into papers.csv

It makes use of docker to avoid python environment headaches. To run the example

    ./run.sh
