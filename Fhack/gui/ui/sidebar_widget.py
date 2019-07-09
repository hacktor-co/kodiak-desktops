#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - side bar menu ui's code
"""

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QPushButton, QFrame
)


class SideBarWidget(QWidget):

    def __init__(self, parent=None):
        super(SideBarWidget, self).__init__(parent)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet(
            """
                background-color: #2fb5b6;
                min-width: 120px;
                max-width: 120px;
                min-height: 790px;
                max-height: 790px;
                padding: 0;
            """
        )

        sidebar_layout.addWidget(self.__icon_holder_frame__())
        sidebar_layout.addWidget(self.__tools_menu_button__())
        sidebar_layout.addWidget(self.__notification_menu_button__())
        sidebar_layout.addWidget(self.__report_menu_button__())
        sidebar_layout.addWidget(self.__hackbox_menu_button__())
        sidebar_layout.addWidget(self.__ai_menu_button__())
        sidebar_layout.addWidget(self.__black_store_menu_button__())
        sidebar_layout.addWidget(self.__setting_menu_button__())
        sidebar_layout.addWidget(self.__extra_frame__())

        sidebar_layout.addStretch()
        self.setLayout(sidebar_layout)

    @staticmethod
    def __icon_holder_frame__():
        icon_holder = QLabel()

        image = QPixmap('./assets/index-logo.svg')

        image.scaled(10, 10)

        icon_holder.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        icon_holder.setPixmap(image)

        icon_holder.setStyleSheet(
            """
                max-height: 60px;
                min-height: 60px;
                min-width: 120px;
                max-width: 120px;
            """
        )

        return icon_holder

    @staticmethod
    def __tools_menu_button__():
        button = QPushButton("tools")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
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
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
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
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
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
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
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
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
            """
        )

        return button

    @staticmethod
    def __black_store_menu_button__():
        button = QPushButton("black store")
        button.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 100px;
                min-height: 100px;
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
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
                min-width: 116px;
                max-width: 116px;
                border: 2px solid #2c3a47;
                border-bottom: 1px solid #000;
            """
        )

        return button

    @staticmethod
    def __extra_frame__():
        frame = QFrame()
        frame.setStyleSheet(
            """
                background-color: #2c3a47;
                max-height: 8px;
                min-height: 8px;
            """
        )

        return frame
