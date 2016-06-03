#!/usr/bin/env python

import sys

if sys.version_info < (3, 0):
    import ConfigParser
    from ConfigParser import SafeConfigParser
else:
    import configparser as ConfigParser
    from configparser import SafeConfigParser


class SecudepConfig(object):
    def __init__(self, file):
        config = SafeConfigParser()
        config.read(file)

        try:
            # General
            self._webroot = config.get('General', 'webroot')
            self._kernel = config.get('General', 'kernel')
            self._initrd = config.get('General', 'initrd')
            self._params = config.get('General', 'params')
            self._destdir = config.get('General', 'destdir')

            # Codesign
            self._signkey = config.get('Codesign', 'key')
            self._signcert = config.get('Codesign', 'cert')

        except ConfigParser.NoOptionError as ex:
            print(ex)
            sys.exit(1)
