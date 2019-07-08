#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - side bar menu ui's code
"""

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QPushButton
)


class SideBarWidget(QWidget):

    def __init__(self, parent=None):
        super(SideBarWidget, self).__init__(parent)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet(
            """
                min-width: 120px;
                max-width: 120px;
                min-height: 790px;
                max-height: 790px;
                padding: 0;
            """
        )

        sidebar_layout.addWidget(self.__sidebar_frame__())
        sidebar_layout.addWidget(self.__tools_menu_button__())
        sidebar_layout.addWidget(self.__notification_menu_button__())
        sidebar_layout.addWidget(self.__report_menu_button__())
        sidebar_layout.addWidget(self.__hackbox_menu_button__())
        sidebar_layout.addWidget(self.__ai_menu_button__())
        sidebar_layout.addWidget(self.__setting_menu_button__())

        sidebar_layout.addStretch()
        self.setLayout(sidebar_layout)

    @staticmethod
    def __sidebar_frame__():
        icon_holder = QLabel()
        icon_holder.setStyleSheet(
            """
                background-color: #2fb5b6;
                max-height: 60px;
                min-height: 60px;
                min-width: 120px;
                max-width: 120px;
            """
        )

        return icon_holder

    @staticmethod
    def __tools_menu_button__():
        button = QPushButton("Tools")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 120px;
                max-width: 120px; 
                margin-bottom: 1px;
            """
        )

        return button

    @staticmethod
    def __notification_menu_button__():
        button = QPushButton("notification")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 120px;
                max-width: 120px; 
                margin-bottom: 1px;
            """
        )

        return button

    @staticmethod
    def __report_menu_button__():
        button = QPushButton("report")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 120px;
                max-width: 120px; 
                margin-bottom: 1px;
            """
        )

        return button

    @staticmethod
    def __hackbox_menu_button__():
        button = QPushButton("hackbox")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 120px;
                max-width: 120px; 
                margin-bottom: 1px;
            """
        )

        return button

    @staticmethod
    def __ai_menu_button__():
        button = QPushButton("ai")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 120px;
                max-width: 120px; 
                margin-bottom: 1px;
            """
        )

        return button

    @staticmethod
    def __setting_menu_button__():
        button = QPushButton("setting")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 120px;
                max-width: 120px; 
                margin-bottom: 1px;
            """
        )

        return button
