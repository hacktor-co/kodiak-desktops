"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - This package handle hyper application that user select which kind of
        application want to run, gui base or console base
"""

from sys import argv

from incommon.constants.console_color import ConsoleColor
from incommon.utils.os_helper import get_os_info


def main():
    try:

        if str(argv[1]).lower() == "-c":
            from console.console_base import main as console_main
            console_main()
        elif str(argv[1]).lower() == "-g":
            from gui.gui_base import main as gui_main
            gui_main()
        elif str(argv[1]).lower() == "-h":
            print(
               ConsoleColor.MAGENTA + """
                Thank you for using hyper => Hyper arguments is
                    -c : for console base hyper
                    -g : for gui base hyper
                    -h : for see this text
                
                @ http://hacktor.co
                """ + ConsoleColor.WHITE
            )
        else:
            from gui.gui_base import main as gui_main
            gui_main()

    except IndexError:
        from gui.gui_base import main as gui_main
        gui_main()


if __name__ == '__main__':
    main()
