#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - side bar menu ui's code
"""

from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtWidgets import (
    QWidget, QFrame, QBoxLayout
)


class SideBarWidget(QWidget):

    def __init__(self, parent=None):
        super(SideBarWidget, self).__init__(parent)

        sidebar_layout = QBoxLayout(QBoxLayout.TopToBottom)
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(
            """
                background-color: #000;
                min-width: 150px;
                max-width: 150px;
                min-height: 790px;
                max-height: 790px;
            """
        )

        sidebar_layout.addWidget(self.__sidebar_frame__(), 0)

        self.setLayout(sidebar_layout)

    @staticmethod
    def __sidebar_frame__():
        frame = QFrame()

        return frame
