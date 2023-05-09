#!/usr/bin/env bash
# See README.md
set -ex

image_name=s2-folks.download_pmids

cd "$(dirname "$0")"

docker build . -t "$image_name"
docker run -v "$(pwd):/root" "$image_name" python get_papers.py
