#!/usr/bin/python3

"""
    - Created on jun 5/2019 by [topcodermc@gmail.com]

    - This package hanle Fhack application execution that user can
     execute this as console application or GUI base
"""

try:
    import argparse

    from common.constants.console_color import ConsoleColor

except ImportError as error:
    print("Has problem with importing library in core/Fhack.py as %s" % error)
    raise SystemExit


def main():
    print(ConsoleColor.RED + "Hello this is test")
    argparse.ArgumentParser(
        description=str("<Instagram bruteforce script>\n Created By topcoder.mc")
    )


if __name__ == '__main__':
    main()
