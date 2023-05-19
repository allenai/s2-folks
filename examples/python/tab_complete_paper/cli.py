import re

import click
import requests


def complete_title(ctx, param, incomplete):
    results = requests.get('https://api.semanticscholar.org/graph/v1/paper/autocomplete',
                           params={'query': incomplete}).json()
    completions = []
    for paper in results.get('matches', []):
        cleaned_title = re.sub('[^\\w ]', '', paper['title'].lower())
        if cleaned_title.startswith(incomplete):
            completions.append(cleaned_title)
    return completions


@click.command()
@click.argument('title', shell_complete=complete_title)
def cli(title):
    result = requests.get('https://api.semanticscholar.org/graph/v1/paper/autocomplete',
                               params={'query': title}).json()
    matches = result.get('matches', [])
    if not matches:
        print(f'No paper titles start with: {title}')
    else:
        paper_id = matches[0]['id']
        paper = requests.get(f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=url').json()
        print(paper['url'])


if __name__ == '__main__':
    cli()
