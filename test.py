# !/usr/bin/python

import os

packages = list()

for root, dirs, files in os.walk("./Fhack", topdown=False):
    for name in files:
        if name.endswith("pyc"):
            continue
        elif name.startswith('__init__'):
            continue
        else:
            packages.append(os.path.join(root, name)[2:])
    for name in dirs:
        packages.append(os.path.join(root, name)[2:])


for item in packages:
    print(item)
