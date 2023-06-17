import argparse
import os

import requests

S2_API_KEY = os.getenv('S2_API_KEY')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paper_id',
                        help='Any paper ID accepted by the Semantic Scholar API, e.g. CorpusID:123')
    args = parser.parse_args()

    paper = get_paper(args.paper_id)
    print(f'"{paper["title"]}" has {len(paper["authors"])} authors.')
    for author in paper['authors']:
        print(f'  {author["name"]}')

    print('Finding citing papers with those authors...')
    citations = get_citations(args.paper_id)
    self_citations = list(filter_self_citing(paper['authors'], citations))
    print(f'Paper has {len(citations)} citations of which {len(self_citations)} contain self-citing authors.')
    for paper, self_citers in self_citations:
        author_names = ', '.join(a['name'] for a in self_citers)
        print(f'  {author_names} in citing paper "{paper["title"]}"')

    print('Finding referenced papers with those authors...')
    references = get_references(args.paper_id)
    self_references = list(filter_self_citing(paper['authors'], references))
    print(f'Paper has {len(references)} references of which {len(self_references)} contain self-referencing authors.')
    for paper, self_referencers in self_references:
        author_names = ', '.join(a['name'] for a in self_referencers)
        print(f'  {author_names} in referenced paper "{paper["title"]}"')


def get_paper(paper_id):
    rsp = requests.get(f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}',
                       headers={'X-API-KEY': S2_API_KEY},
                       params={'fields': 'title,authors'})
    rsp.raise_for_status()
    return rsp.json()


def get_citations(paper_id):
    edges = get_citation_edges(url=f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations',
                               headers={'X-API-KEY': S2_API_KEY},
                               params={'fields': 'title,authors'})
    return list(edge['citingPaper'] for edge in edges)


def get_references(paper_id):
    edges = get_citation_edges(url=f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references',
                               headers={'X-API-KEY': S2_API_KEY},
                               params={'fields': 'title,authors'})
    return list(edge['citedPaper'] for edge in edges)


def get_citation_edges(**req_kwargs):
    """This helps with API endpoints that involve paging."""
    page_size = 1000
    offset = 0
    while True:
        req_kwargs.setdefault('params', dict())
        req_kwargs['params']['limit'] = page_size
        req_kwargs['params']['offset'] = offset
        rsp = requests.get(**req_kwargs)
        rsp.raise_for_status()

        page = rsp.json()["data"]
        for element in page:
            yield element

        if len(page) < page_size:
            break  # no more pages
        offset += page_size


def filter_self_citing(target_authors, papers):
    """Filter papers to those that contain any of the target authors."""
    authors_by_id = {a['authorId']: a for a in target_authors}
    for paper in papers:
        paper_author_ids = {a['authorId'] for a in paper['authors']}
        self_citers = paper_author_ids.intersection(authors_by_id)
        if self_citers:
            yield paper, [authors_by_id[author_id] for author_id in self_citers]


if __name__ == '__main__':
    main()
