This example fetches paper data from a list of PMIDs retrieved from

https://pubmed.ncbi.nlm.nih.gov/?term=p53&filter=pubt.clinicaltrial&filter=pubt.review&filter=years.2020-2020&size=200

and maps JSON returned by the semanticscholar API into papers.csv

It makes use of docker to avoid python environment headaches. To run the example

    ./run.sh

The entire example is dockerized for consistency regardless of host environments. If you are unfamiliar with Docker,
you can learn about it on https://docker-curriculum.com/ or you can translate environmental details in the [Dockerfile] 
to your own preferred python environment (i.e. virtualenv, pyenv, conda). It's really just a few dependencies
in requirements.txt

[Dockerfile]: ./Dockerfile