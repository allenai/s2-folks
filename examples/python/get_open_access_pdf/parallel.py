#!/usr/bin/env python3
import dotenv
dotenv.load_dotenv()

from aiohttp import ClientSession
import argparse
import asyncio
from itertools import islice
import os
from typing import AsyncGenerator, Generator, Iterable, TypeVar, Union

S2_API_KEY = os.environ['S2_API_KEY']

T = TypeVar('T')


def batched(iterable: Iterable[T], n: int) -> Generator[list[T], None, None]:
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


async def get_papers(session: ClientSession, paper_ids: list[str], batch_size = 500, fields: str = 'paperId,title', **kwargs) -> AsyncGenerator[dict, None]:
    for batch in batched(paper_ids, batch_size):
        params = {
            'fields': fields,
            **kwargs,
        }
        headers = {
            'X-API-KEY': S2_API_KEY,
        }
        json = {
            'ids': batch,
        }

        async with session.post(f'https://api.semanticscholar.org/graph/v1/paper/batch', params=params, headers=headers, json=json) as response:
            response.raise_for_status()

            for paper in await response.json():
                yield paper


async def download_pdf(session: ClientSession, url: str, path: str, user_agent: str = 'aiohttp/3.0.0'):
    # send a user-agent to avoid server error
    headers = {
        'user-agent': user_agent,
    }

    # stream the response to avoid downloading the entire file into memory
    async with session.get(url, headers=headers, verify_ssl=False) as response:
        # check if the request was successful
        response.raise_for_status()

        if response.headers['content-type'] != 'application/pdf':
            raise Exception('The response is not a pdf')

        with open(path, 'wb') as f:
            # write the response to the file, chunk_size bytes at a time
            async for chunk in response.content.iter_chunked(8192):
                f.write(chunk)


async def download_papers(paper_ids: list[str], directory: str = 'papers', batch_size: int = 500, user_agent: str = 'aiohttp/3.0.0') -> AsyncGenerator[tuple[str, Union[str, None, Exception]], None]:
    # create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # use a session to reuse the same TCP connection
    async with ClientSession() as session:
        async for paper in get_papers(session, paper_ids, batch_size=batch_size, fields='paperId,isOpenAccess,openAccessPdf'):
            paper_id = paper['paperId']

            # check if the paper is open access
            if not paper['isOpenAccess']:
                yield paper_id, None

            try:
                paperId: str = paper['paperId']
                pdf_url: str = paper['openAccessPdf']['url']
                pdf_path = os.path.join(directory, f'{paperId}.pdf')
                await download_pdf(session, pdf_url, pdf_path)
                yield paper_id, pdf_path
            except Exception as e:
                yield paper_id, e


async def main(args: argparse.Namespace):
    async for paper_id, result in download_papers(args.paper_ids, directory=args.directory, batch_size=args.batch_size, user_agent=args.user_agent):
        if isinstance(result, Exception):
            print(f"Failed to download '{paper_id}': {type(result).__name__}: {result}")
        elif result is None:
            print(f"'{paper_id}' is not open access")
        else:
            print(f"Downloaded '{paper_id}' to '{result}'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', default='papers')
    parser.add_argument('--user-agent', '-u', default='aiohttp/3.0.0')
    parser.add_argument('--batch-size', '-n', type=int, default=500)
    parser.add_argument('paper_ids', nargs='+', default=[])
    args = parser.parse_args()
    asyncio.run(main(args))
