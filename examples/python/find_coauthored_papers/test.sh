#!/usr/bin/env bash
# Minimal script to periodically run this example to see if it still works.
# Runs test.py in a repeatable docker environment.
set -ex

image_name=s2-folks.find_coauthored_papers

cd "$(dirname "$0")"

docker build . -t "$image_name"
docker run -v "$(pwd):/root" "$image_name" python test.py
