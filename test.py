#!/usr/bin/env python3

# just testing noosphere interface

import sys
sys.path.insert(1, '/home/blazeva1/Dropbox/Projects/noosphere')

from noosphere import Noosphere
from noosphere.data import FileDB

nos = Noosphere(FileDB("par.json"))

root = nos.get('!0')
print(root)
plugins = root['plugins']
print(plugins)
for plugin in plugins:
    print(plugin['emits'])
