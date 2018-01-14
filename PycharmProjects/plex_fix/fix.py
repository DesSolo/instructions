#! /usr/bin/python2.7
from re import compile
import os
from shutil import copy2


class FixPlex(object):
    def __init__(self):
        self.re_main = compile('^main-.+[.]js$')
        self.name = self.search('/usr/lib/plexmediaserver/Resources/Plug-ins-f54242b6b/WebClient.bundle/Contents/Resources/js')
        if self.name:
            self.backup()
            self.fix_plex()

    def search(self, dir_path):
        for item in os.listdir(dir_path):
            if self.re_main.match(item):
                return item

    def fix_plex(self):
        button = compile('<li><a class="plex-pass-btn [\s\S]+?</li>')
        with open(self.name) as r_file:
            old_js = r_file.read()
            bad_link = button.search(old_js)
            if bad_link:
                new_js = old_js.replace(bad_link.group(0), '"')
                with open(self.name, 'w') as w_file:
                    w_file.write(new_js)
                print('All done, please restart Plex\nsystemctl restart plexmediaserver')
            else:
                print('Not found items')

    def backup(self):
        name_backup = self.name + '.back'
        copy2(self.name, self.name + '.back')
        print('Backup created ' + name_backup)


FixPlex()
