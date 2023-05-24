import argparse
import re
import sys

import requests


def resolve_author(desc: str):
    req_fields = 'authorId,name,url'

    if re.match('\\d+', desc):  # ID given
        rsp = requests.get(f'https://api.semanticscholar.org/graph/v1/author/{desc}',
                           params={'fields': req_fields})
        rsp.raise_for_status()
        return rsp.json()

    else:  # search
        rsp = requests.get('https://api.semanticscholar.org/graph/v1/author/search',
                           params={'query': desc, 'fields': req_fields})
        rsp.raise_for_status()

        results = rsp.json()
        if results['total'] == 0:  # no results
            print(f'Could not find author "{desc}"')
            sys.exit(1)
        elif results['total'] == 1:  # one unambiguous match
            return results['data'][0]
        else:  # multiple matches
            print(f'Multiple authors matched "{desc}".')
            for author in results['data']:
                print(author)
            print('Re-run with a specific ID.')
            sys.exit(1)


def get_author_papers(author_id):
    rsp = requests.get(f'https://api.semanticscholar.org/graph/v1/author/{author_id}/papers',
                       params={'fields': 'title,url,year', 'limit': 1000})
    rsp.raise_for_status()
    return rsp.json()['data']


def find_coauthored_papers(left_author_id, right_author_id):
    left_papers = get_author_papers(left_author_id)
    right_papers = get_author_papers(right_author_id)

    left_paper_ids = set(p['paperId'] for p in left_papers)
    right_paper_ids = set(p['paperId'] for p in right_papers)
    coauthored_paper_ids = left_paper_ids.intersection(right_paper_ids)
    coauthored_papers = [p for p in left_papers if p['paperId'] in coauthored_paper_ids]
    # most recent first, sort by title within any year
    return sorted(coauthored_papers, key=lambda p: (-p['year'], p['title']))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('left_author')
    parser.add_argument('right_author')
    args = parser.parse_args()

    left_author = resolve_author(args.left_author)
    print(f"Left author: {left_author['name']} {left_author['url']}")
    right_author = resolve_author(args.right_author)
    print(f"Right author: {right_author['name']} {right_author['url']}")

    coauthored_papers = find_coauthored_papers(left_author['authorId'], right_author['authorId'])
    print(f'Found {len(coauthored_papers)} coauthored papers')
    for paper in coauthored_papers:
        print(f'{paper["year"]} {paper["title"]} {paper["url"]}')


if __name__ == '__main__':
    main()
