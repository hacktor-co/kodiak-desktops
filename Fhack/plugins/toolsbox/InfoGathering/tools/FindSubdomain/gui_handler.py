#!usr/bin/python3.7
"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow)


class MainWindow(QMainWindow):

    def init(self, parent):
        super().__init__()

    def execute_app(self, parent=None):
        self.init(parent)
        self.show()
