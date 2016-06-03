#!/usr/bin/env python

import sys

if sys.version_info < (3, 0):
    import ConfigParser as configparser
else:
    import configparser


class SecudepConfigError(Exception):
    pass


class SecudepConfig(object):
    def __init__(self, file):
        config = configparser.SafeConfigParser()
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

        except configparser.NoOptionError as ex:
            raise SecudepConfigError(ex)
