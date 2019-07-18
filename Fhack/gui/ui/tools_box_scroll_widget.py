#!/usr/bin/python3
"""
    - Created on jul 13/2019 - hacktorco
    - All rights reserved for hacktor team

    - scroll bar for tools box widget to show all tool headers
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox
)

from gui.common.styles.tools_box_scroll_widget_styles import *


class ToolsBoxScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsBoxScrollWidget, self).__init__(parent)

        if self.isHidden() is not True:

            self.setStyleSheet(main_widget_style)

            formLayout = QFormLayout()

            groupBox = QGroupBox()
            groupBox.setStyleSheet("""
                background-color: red;
            """)
            groupBox.setContentsMargins(0, 0, 0, 0)

            for i in range(10):
                button = QPushButton("Click Me")
                button.setStyleSheet("""
                    background-color: green;
                    color: white;
                    min-height: 90px;
                    max-height: 90px;
                    min-width: 150px;
                """)
                formLayout.addRow(button)

            groupBox.setLayout(formLayout)

            scroll = QScrollArea()
            scroll.setStyleSheet("""
                min-width: 200px;
            """)
            scroll.setWidget(groupBox)

            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addStretch()

            layout.addWidget(scroll)
