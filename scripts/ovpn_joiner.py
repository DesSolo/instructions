#! /usr/bin/python2.7

from re import compile
from os import path
import ConfigParser
from sys import argv


class JoinVPNCrt(object):
    def __init__(self, name):
        name = name.split('.')[0]
        self.name = name
        self.ca = 'ca.crt'
        self.crt = name + '.crt'
        self.key = name + '.key'
        self.status = self._check()
        self.ca_rex = compile('-----[\s\S]+-----[\s\S]+-----[\s\S]+-----')
        self._get_config()

    def _get_config(self):
        conf = ConfigParser.ConfigParser()
        conf.read('config.conf')
        header = conf.get('Main', 'header')
        self.header = header.format(self.get_certs('ca.crt'), self.get_certs(self.crt), self.get_certs(self.key))

    def _manual_check(self):
        for item in [self.ca, self.crt, self.key]:
            if not path.isfile(item):
                print item, 'Not found'

    def _check(self):
        if all([path.isfile(self.ca), path.isfile(self.crt), path.isfile(self.key)]):
            return True
        else:
            self._manual_check()
            return False

    def get_certs(self, name):
        if self.status:
            with open(name) as file:
                return self.ca_rex.search(file.read()).group(0)
        else:
            return 'Error'

    def join_cert(self):
        if self.status:
            with open(self.name + '.ovpn', 'w') as file:
                file.write(self.header)
            print 'Complete', self.name + '.ovpn', 'created'
        else:
            print 'Error'

if __name__ == '__main__':
    joiner = JoinVPNCrt(argv[-1])
    joiner.join_cert()
