#!/bin/sh

set -e

docker build -t thesis --rm .
docker run --rm thesis cat thesis.pdf >thesis.pdf
ls -l thesis.pdf
