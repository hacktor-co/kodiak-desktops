#!/usr/bin/python3
"""
    - Created on jul 13/2019 - hacktorco
    - All rights reserved for hacktor team

    - scroll bar for tools box widget to show all tool headers
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton
)

from gui.common.styles.tools_box_scroll_widget import *


class ToolsBoxScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsBoxScrollWidget, self).__init__(parent)

        self.setStyleSheet(main_widget_style)
        self.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()

        # Container Widget
        widget = QWidget()
        widget.setContentsMargins(0, 0, 0, 0)

        # Layout of Container Widget
        for _ in range(100):
            btn = QPushButton("test")
            layout.addWidget(btn)
        widget.setLayout(layout)

        # Scroll Area Properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(widget)

        # Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

        self.setLayout(layout)
