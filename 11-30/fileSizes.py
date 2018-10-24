#! /usr/bin/env python3

import os

pathname = '/Users/bronson/Downloads'
totalSize = 0

for filename in os.listdir(pathname):
    # Skip to next filename if the current item is not a file:
    if not os.path.isfile(os.path.join(pathname, filename)):
        continue
    # Add to totalSize if the the current item is a file:
    totalSize += os.path.getsize(os.path.join(pathname, filename))

print(totalSize)
