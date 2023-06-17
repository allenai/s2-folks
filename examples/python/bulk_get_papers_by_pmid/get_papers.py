#!/usr/bin/env python3
import dotenv
dotenv.load_dotenv()

import argparse
import csv
import os
from requests import Session
from typing import Generator, TypeVar

S2_API_KEY = os.environ.get('S2_API_KEY', '')

T = TypeVar('T')


def batched(items: list[T], batch_size: int) -> list[T]:
    return [items[i:i + batch_size] for i in range(0, len(items), batch_size)]


def get_paper_batch(session: Session, ids: list[str], fields: str = 'paperId,title', **kwargs) -> list[dict]:
    params = {
        'fields': fields,
        **kwargs,
    }
    headers = {
        'X-API-KEY': S2_API_KEY,
    }
    body = {
        'ids': ids,
    }

    # https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/post_graph_get_papers
    with session.post('https://api.semanticscholar.org/graph/v1/paper/batch',
                       params=params,
                       headers=headers,
                       json=body) as response:
        response.raise_for_status()
        return response.json()


def get_papers(ids: list[str], batch_size: int = 100, **kwargs) -> Generator[dict, None, None]:
    # use a session to reuse the same TCP connection
    with Session() as session:
        # take advantage of S2 batch paper endpoint
        for ids_batch in batched(ids, batch_size=batch_size):
            yield from get_paper_batch(session, ids_batch, **kwargs)


def main(args: argparse.Namespace) -> None:
    with open(args.pmid_file, 'r') as pmid_file:
        pmids = [line.strip() for line in pmid_file.readlines()]

    count = 0

    with open(args.output, 'w') as csvfile:
        fieldnames = ['pmid', 'title', 'first_author', 'year', 'abstract']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        ids = [f'PMID:{pmid}' for pmid in pmids]
        fields = 'externalIds,title,authors,year,abstract'

        for paper in get_papers(ids, fields=fields):
            # If an ID is not found, the corresponding entry in the response will be null.
            if not paper:
                continue

            paper_authors = paper.get('authors', [])
            writer.writerow({
                'pmid': paper['externalIds']['PubMed'],
                'title': paper['title'],
                'first_author': paper_authors[0]['name'] if paper_authors else '<no_author_data>',
                'year': paper['year'],
                'abstract': paper['abstract'],
            })
            count += 1

    print(f'Wrote {count} results to {args.output}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', default='papers.csv')
    parser.add_argument('pmid_file', nargs='?', default='pmid-p53-set.txt')
    args = parser.parse_args()
    main(args)
