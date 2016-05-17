#!/bin/sh

set -e

git apply ipxe.patch

cp ipxe.patch ipxe.patch.orig
git diff >ipxe.patch

CERTS=cert.cer
make EMBED=boot.ipxe CERT=${CERTS}
