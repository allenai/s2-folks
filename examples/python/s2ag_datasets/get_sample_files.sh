#!/usr/bin/env bash
# Grabbing sample files is described in the "README" property of a release.
# See https://api.semanticscholar.org/datasets/v1/release/latest
for f in $(curl -s https://s3-us-west-2.amazonaws.com/ai2-s2ag/samples/MANIFEST.txt)
  do curl --create-dirs "https://s3-us-west-2.amazonaws.com/ai2-s2ag/$f" -o "$f" -s
  echo "$f"
done

gunzip -qf samples/*/*.gz
