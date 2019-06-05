#!/usr/bin/python3

__setup__ = {
    "Name": "Fhack",
    "version": "1.2.9.45",
    "packages": ['Fhack', ],
    "license": "GNU GENERAL PUBLIC LICENSE V2",
    "description": "README.md"
}

from setuptools import setup

def main():

    setup(
        # basic stuff here
        name='Fhack',
        version='1.0.0.1',
        description='Fhack pen-test tools',
        author='Hacktor',
        author_email='hacktor@hacktor.co',
        license="GNU GENERAL PUBLIC LICENSE V2",
        url='http://www.hacktor.co',
        scripts=[
            './Fhack/Fhack.py'
        ]
    )


if __name__ == '__main__':
    main()
