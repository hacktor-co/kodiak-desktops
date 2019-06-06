#!/usr/bin/python3
# -*- coding: utf-8 -*-

# todo: must fix script installer in linux

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'Fhack'
DESCRIPTION = 'Fhack pentest-tool'
URL = 'https://github.com/hacktorco/Fhack'
EMAIL = 'hacktor@hacktor.co'
AUTHOR = 'Hacktor'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.0.0.1'

REQUIRED = []

EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

packages = list()
packages.append('Fhack')
for root, dirs, files in os.walk("./Fhack", topdown=False):
    for name in files:
        if name.endswith("pyc"):
            continue
        elif name.startswith('__init__'):
            continue
        elif name.endswith('py'):
            continue
        else:
            packages.append(os.path.join(root, name)[2:])
    for name in dirs:
        packages.append(os.path.join(root, name)[2:])


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=packages,
    # find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "docs"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    # scripts=scripts,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='GPLv2',
    classifiers=[
        # Trove classifiers
        'License :: OSI Approved :: GPLv2 License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
