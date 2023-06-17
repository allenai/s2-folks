import os
import re

import requests

S2_API_KEY = os.getenv('S2_API_KEY')
result_limit = 10


def main():
    basis_paper = find_basis_paper()
    find_recommendations(basis_paper)


def find_basis_paper():
    papers = None
    while not papers:
        query = input('Find papers about what: ')
        if not query:
            continue

        rsp = requests.get('https://api.semanticscholar.org/graph/v1/paper/search',
                           headers={'X-API-KEY': S2_API_KEY},
                           params={'query': query, 'limit': result_limit, 'fields': 'title,url'})
        rsp.raise_for_status()
        results = rsp.json()
        total = results["total"]
        if not total:
            print('No matches found. Please try another query.')
            continue

        print(f'Found {total} results. Showing up to {result_limit}.')
        papers = results['data']
        print_papers(papers)

    selection = ''
    while not re.fullmatch('\\d+', selection):
        selection = input('Select a paper # to base recommendations on: ')
    return results['data'][int(selection)]


def find_recommendations(paper):
    print(f"Up to {result_limit} recommendations based on: {paper['title']}")
    rsp = requests.get(f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{paper['paperId']}",
                       headers={'X-API-KEY': S2_API_KEY},
                       params={'fields': 'title,url', 'limit': 10})
    rsp.raise_for_status()
    results = rsp.json()
    print_papers(results['recommendedPapers'])


def print_papers(papers):
    for idx, paper in enumerate(papers):
        print(f"{idx}  {paper['title']} {paper['url']}")


if __name__ == '__main__':
    main()
