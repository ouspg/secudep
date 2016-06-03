#!/usr/bin/env python

from __future__ import absolute_import

import subprocess
import urllib

from urlparse import urlparse
from optparse import OptionParser

from .config import SecudepConfig


def main():
    usage = "usage: %prog <config>"
    parser = OptionParser(usage)

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("You need to supply config")

    config_file = args[0]
    config = SecudepConfig(config_file)

    ipxe_config = config._destdir + "/start.ipxe"
    write_start_ipxe(
        ipxe_config,
        config._kernel,
        config._initrd,
        config._params
    )

    for target in [ipxe_config, config._kernel, config._initrd]:
        write_sign_file(
            "{0}/{1}.sig".format(config._destdir, filename_from_url(target)),
            config._signkey,
            config._signcert,
            target
        )


def write_sign_file(destination, key, cert, file):
    with open(destination, "w") as dest:
        sig = sign_binary(key, cert, file)
        dest.write(sig)
    print("Wrote file {0}".format(destination))


def write_start_ipxe(destination, kernel, initrd, params):
    kernel_name = filename_from_url(kernel)
    initrd_name = filename_from_url(initrd)

    start_dot_ipxe = [
        r"#!ipxe",
        r"kernel {0} {1}".format(kernel, params),
        r"imgverify {0} {0}.sig".format(kernel_name),
        r"initrd {0}".format(initrd),
        r"imgverify {0} {0}.sig".format(initrd_name),
        r"boot",
        r""
    ]

    with open(destination, "w") as dest:
        dest.write("\n".join(start_dot_ipxe))
    print("Wrote file {0}".format(destination))


def write_boot_ipxe(webroot):
    boot_dot_ipxe = [
        r"#!ipxe",
        r"imgtrust --permanent",
        r"dhcp",
        r"echo",
        r"prompt --key c --timeout 2000 Press 'c' for the iPXE command line... && shell ||",
        r"imgfetch {0}/start.ipxe".format(webroot),
        r"imgverify start.ipxe {0}/start.ipxe.sig".format(webroot),
        r"chain start.ipxe"
        r""
    ]
    return "\n".join(boot_dot_ipxe)


def sign_binary(key, cert, file):
    cmd = [
        "openssl",
        "smime",
        "-sign",
        "-binary",
        "-noattr",
        "-signer", "{0}".format(cert),
        "-inkey", "{0}".format(key),
        "-outform", "DER"
    ]

    try:
        source = urllib.urlopen(file)

        if source.getcode() is not None and source.getcode() != 200:
            raise Exception("File not found")

        proc = subprocess.Popen(
            cmd,
            stdin=source,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        (stdout, stderr) = proc.communicate()

    finally:
        source.close()

    if proc.returncode > 0:
        print(stderr)
        raise Exception("OpenSSL barfed")

    return stdout


def filename_from_url(url):
    return urlparse(url).path.split("/")[-1]


if __name__ == '__main__':
    main()
