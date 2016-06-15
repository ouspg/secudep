#!/usr/bin/env python

from __future__ import absolute_import

import errno
import os
import os.path
import subprocess
import urllib

from urlparse import urlparse
from optparse import OptionParser

from .config import SecudepConfig, SecudepConfigError


def main():
    usage = "usage: %prog <config>"
    parser = OptionParser(usage)

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("You need to supply config")

    try:
        config_file = args[0]
        config = SecudepConfig(config_file)
    except SecudepConfigError as ex:
        print(ex)
        sys.exit(1)

    menu = ipxe_menu(config)
    start_ipxe = None
    signkey = None
    signcert = None

    for section in config.sections():
        conf_sect = config.section(section)
        if start_ipxe is None:
            start_ipxe = os.path.join(
                conf_sect['destdir'], "start.ipxe"
            )
            signkey = conf_sect['signkey']
            signcert = conf_sect['signcert']

        menu_entry = ipxe_menu_entry(section, conf_sect)
        menu = menu + "\n" + menu_entry
        handle_section(section, conf_sect)

    with open(start_ipxe, "w") as dest:
              dest.write(menu)
    write_sign_file(start_ipxe + ".sig", signkey, signcert, start_ipxe)


def handle_section(name, config):
    kernel = config['kernel']
    initrd = config['initrd']
    destdir = os.path.join(config['destdir'], name)
    signkey = config['signkey']
    signcert = config['signcert']

    for target in [kernel, initrd]:
        dest = "{0}/{1}.sig".format(destdir, filename_from_url(target))
        write_sign_file(dest, signkey, signcert, target)


def write_sign_file(destination, key, cert, file):
    try:
        os.mkdir(os.path.dirname(destination))
    except OSError as exc:
        if exc.args[0] is not errno.EEXIST:
            raise
    sig = sign_binary(key, cert, file)
    with open(destination, "w") as dest:
        dest.write(sig)
    print("Wrote file {0}".format(destination))


def ipxe_menu(config):
    ipxe_menu = [
        r"#!ipxe",
        r"",
        r"menu Select:"
    ]

    for sect in config.sections():
        entry = r"item {0} {1}".format(sect, config.section(sect)['name'])
        ipxe_menu.append(entry)

    ipxe_menu.append(r"choose target && goto ${target}")
    ipxe_menu.append(r"")
    return '\n'.join(ipxe_menu)


def ipxe_menu_entry(name, config):
    r"""
    >>> config = {
    ...     'name': 'Test Name',
    ...     'kernel': 'http://example.com/path/to/kernel',
    ...     'initrd': 'http://example.com/path/to/initrd',
    ...     'params': 'kernel params'
    ... }
    >>> print ipxe_menu_entry('example', config)
    :example
    kernel http://example.com/path/to/kernel kernel params
    imgverify kernel example/kernel.sig
    initrd http://example.com/path/to/initrd
    imgverify initrd example/initrd.sig
    boot
    <BLANKLINE>
    """
    kernel = config['kernel']
    initrd = config['initrd']
    params = config['params']
    kernel_name = filename_from_url(kernel)
    initrd_name = filename_from_url(initrd)

    menu_entry = [
        r":{0}".format(name),
        r"kernel {0} {1}".format(kernel, params),
        r"imgverify {0} {1}/{0}.sig".format(kernel_name, name),
        r"initrd {0}".format(initrd),
        r"imgverify {0} {1}/{0}.sig".format(initrd_name, name),
        r"boot",
        r""
    ]
    return '\n'.join(menu_entry)


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
