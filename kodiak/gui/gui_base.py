#!/usr/bin/python3

"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - This package that handle Fhack gui app
"""

import sys

from PyQt5.QtWidgets import QApplication

from gui.ui.mainpage.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
