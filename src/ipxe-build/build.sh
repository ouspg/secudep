#!/bin/sh

set -e

git apply ipxe.patch

cp ipxe.patch ipxe.patch.orig
git diff >ipxe.patch

CERTS="cert.pem"

if [ -f "codesign.pem" ]; then
    CERTS="${CERTS},codesign.pem"
fi

make EMBED=boot.ipxe TRUST=${CERTS}
