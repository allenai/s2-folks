import csv

import requests


def chunks(items, chunk_size):
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def fetch_paper_batch(pmids):
    req = {'ids': [f'PMID:{pmid}' for pmid in pmids]}
    # https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/post_graph_get_papers
    rsp = requests.post('https://api.semanticscholar.org/graph/v1/paper/batch'
                        '?fields=externalIds,title,authors,year,abstract',
                        json=req)
    if rsp.status_code != 200:
        raise Exception(f'Problem fetching {req}: ' + rsp.text)
    return rsp.json()


pmids = [line.strip() for line in open('pmid-p53-set.txt').readlines()]
dest = 'papers.csv'
count = 0
with open(dest, 'w') as fp:
    csvfile = csv.DictWriter(fp, ['pmid', 'title', 'first_author', 'year', 'abstract'])
    csvfile.writeheader()

    # groups of 100 to take advantage of S2 batch paper endpoint
    for pmid_batch in chunks(pmids, 100):
        papers = fetch_paper_batch(pmid_batch)

        for paper in papers:
            csvfile.writerow({
                'pmid': paper['externalIds']['PubMed'],
                'title': paper['title'],
                'first_author': paper['authors'][0]['name'],
                'year': paper['externalIds']['PubMed'],
                'abstract': paper['abstract'],
            })
            count += 1

print(f'Wrote {count} results to {dest}')
