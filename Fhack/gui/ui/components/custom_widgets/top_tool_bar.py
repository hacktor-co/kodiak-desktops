#!/usr/bin/python3
"""
    - Created on jul 31/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package get all tools in toolbox from parent class then
        show it with scroll widget
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox, QHBoxLayout
)


class TopToolBar(QWidget):
    def __init__(self, parent=None):
        super(TopToolBar, self).__init__(parent)

        layout_main = QHBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.addStretch()
        self.setStyleSheet("""
            margin-top: 10px;
            min-width: 770px;
            max-width: 770px;
            background-color: red;
            min-height: 100px;
            max-height: 100px;
        """)

        button = QPushButton("1")
        button.setStyleSheet("""
            min-width: 100px;
            max-width: 100px;
            min-height: 100px;
            margin-right: 20px;
            max-height: 100px;
        """)
        layout_main.addWidget(button)
        button = QPushButton("2")
        button.setStyleSheet("""
            min-width: 100px;
            max-width: 100px;
            min-height: 100px;
            max-height: 100px;
        """)
        layout_main.addWidget(button)
        button = QPushButton("3")
        button.setStyleSheet("""
            min-width: 100px;
            max-width: 100px;
            min-height: 100px;
            max-height: 100px;
        """)
        layout_main.addWidget(button)

        self.setLayout(layout_main)
