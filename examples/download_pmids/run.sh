#!/usr/bin/env bash
set -ex

cd "$(dirname "$0")"

docker build . -t s2-folks.download_pmids
docker run -v "$(pwd):/root" s2-folks.download_pmids python get_papers.py
