#!/bin/sh

set -e

git apply ipxe.patch

cp ipxe.patch ipxe.patch.orig
git diff >ipxe.patch

CERTS=$(ls -m *.pem | tr -d ' ')

make EMBED=boot.ipxe TRUST=${CERTS}
