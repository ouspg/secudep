#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

from optparse import OptionParser
from urlparse import urlparse
from subprocess import call


def main():
    usage = "usage: %prog [options] <url>"
    parser = OptionParser(usage)

    # parser.add_option("-c", "--confidentiality", action="store_true",
    #                   dest="confidentiality", default=False,
    #                   help="Enable confidentiality (Warning: Not safe!).")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("You need to supply url")

    url = urlparse(args[0])
    if not url:
        raise RuntimeError

    if url.scheme != "https":
        print("Please, use HTTPS URL")
        return 1

    if url.port:
        url_port = ":{0}".format(url.port)
        host = url.netloc.strip(url_port)
        port = url.port
    else:
        host = url.netloc
        port = 443

    # Extract certificate over TLS connection from <host>:<port>
    call(["./x509extract/x509extract", host, str(port)])

    # Move extracted cert to ipxe-build/cert.cer and build ipxe
    call(["mv", "{0}.cer".format(host), "ipxe-build/cert.cer"])
    call(["make", "-C ipxe-build", "TAG={0}".format(host)])


def ipxe_first_boot_script(chain_url, sleep=3, dhcp=True):
    r"""
    Generate script which is embedded inside iPXE build

    >>> ipxe_first_boot_script(2)
    Traceback (most recent call last):
    ...
    ValueError: Invalid URL given 2
    """

    if not isinstance(chain_url, basestring):
        raise ValueError("Invalid URL given {0}".format(chain_url))

    url = urlparse(chain_url)

    if url.scheme != "https":
        raise ValueError("Use HTTPS URL")

    if dhcp:
        dhcp_str = "dhcp"
    else:
        dhcp_str = "# dhcp"

    if sleep < 0:
        raise ValueError("Sleep can't be negative")

    boot_ipxe = b"#!ipxe\n" + \
                b"{0}\n".format(dhcp_str) + \
                b"echo\n" + \
                b"echo Continuing boot in {0} seconds..\n".format(sleep) + \
                b"sleep {0}\n".format(sleep) + \
                b"chain {0}\n".format(chain_url)

    return boot_ipxe


if __name__ == "__main__":
    main()
