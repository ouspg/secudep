#!/usr/bin/env python

import sys

if sys.version_info < (3, 0):
    import ConfigParser as configparser
else:
    import configparser


class SecudepConfigError(Exception):
    pass


class SecudepConfig(object):
    _options = [ 'name', 'kernel', 'initrd', 'params', 'webroot',
                 'destdir', 'signkey', 'signcert' ]
    _section = dict()

    def __init__(self, file):
        config = configparser.SafeConfigParser()
        config.read(file)

        for sect in config.sections():
            self._section[sect] = dict()

            try:
                for opt in self._options:
                    self._section[sect][opt] = config.get(sect, opt)
            except configparser.NoOptionError as ex:
                raise SecudepConfigError(ex)

    def sections(self):
        return self._section.keys()

    def section(self, section):
        return self._section[section]
