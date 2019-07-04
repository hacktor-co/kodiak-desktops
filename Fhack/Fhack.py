#!/usr/bin/python3

"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - This package hanle Fhack application that user select which kind of
        application want to run, gui base or console base
"""

from sys import argv

from common.constants.console_color import ConsoleColor
from core.console.console_base import main as console_main
from core.gui.gui_base import main as gui_main


def main():
    try:

        if str(argv[1]).lower() == "-c":
            console_main()
        elif str(argv[1]).lower() == "-g":
            gui_main()
        elif str(argv[1]).lower() == "-h":
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
            gui_main()

    except IndexError:
        gui_main()


if __name__ == '__main__':
    main()
