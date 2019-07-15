#!/usr/bin/python3
"""
    - Created on jul 13/2019 - hacktorco
    - All rights reserved for hacktor team

    - scroll bar for tools box widget to show all tool headers
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

from gui.common.styles.tools_box_scroll_widget import *


class ToolsBoxScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsBoxScrollWidget, self).__init__(parent)

        self.setStyleSheet(main_widget_style)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignRight)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()

        label = QLabel("Hell this is test for scroll view")
        layout.addWidget(label)
        self.setLayout(layout)
