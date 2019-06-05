#!/usr/bin/python3

"""
    - Created on jun 5/2019 by [topcodermc@gmail.com]

    - This package hanle Fhack console
"""

from sys import argv

from common.constants.console_color import ConsoleColor
from console.console_base import main as console_main
from gui.gui_base import main as gui_main


def main():

    try:

        if argv[1] == "-c":
            console_main()
        elif argv[1] == "-g":
            gui_main()
        elif argv[1] == "-h":
            print(
               ConsoleColor.MAGENTA + """
                Thank you for using fhack => Fhack arguments is
                    -c : for console base fhack
                    -g : for gui base fhack
                    -h : for see this text
                
                @ http://hacktor.co
                """ + ConsoleColor.WHITE
            )
        else:
            console_main()

    except IndexError:
        console_main()


if __name__ == '__main__':
    main()
