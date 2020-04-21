#!/usr/bin/python3

"""
    - Created on jun 5/2019 by [topcodermc@gmail.com]

    - This package hanle Fhack console colors
"""

from colorama import init, Fore

class ConsoleColor:
    def __init__(self):
        init()

    RED = Fore.RED
    GREEN = Fore.GREEN
    BLACK = Fore.BLACK
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
    LIGHTBLUE = Fore.LIGHTBLUE_EX
