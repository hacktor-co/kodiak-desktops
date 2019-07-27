#!/usr/bin/python3
"""
    - Created on jul 28/2019 - hacktorco
    - All rights reserved for hacktor team

    - all tools that tool category (tool box) contain's are here
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox
)

class ToolsBoxHolderWidget(QWidget):
    def __init__(self, parent=None, boxname: str = ""):
        super(ToolsBoxHolderWidget, self).__init__(parent)
        print(boxname + " ID: " + str(id(self)))

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

        self.create_widget(boxname)

    def create_widget(self, boxname):

        for i in reversed(range(self.layout.count())):
            if i == 0:
                break
            self.layout.itemAt(1).widget().deleteLater()

        if boxname == "WebTools":
            self.setStyleSheet("""
                        min-width: 830px;
                        max-width: 830px;
                        background-color: red;
                    """)
            button = QPushButton("Hello1")
            self.layout.addWidget(button)
        elif boxname == "NetworkTools":
            self.setStyleSheet("""
                        min-width: 830px;
                        max-width: 830px;
                        background-color: cyan;
                    """)
            button = QPushButton("Hello2")
            self.layout.addWidget(button)
        elif boxname == "LocalAppTools":
            self.setStyleSheet("""
                               min-width: 830px;
                               max-width: 830px;
                               background-color: green;
                           """)
            button = QPushButton("Hello3")
            self.layout.addWidget(button)
