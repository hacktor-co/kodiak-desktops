#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - side bar menu ui's code
"""
from functools import partial

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QPushButton, QFrame, QScrollArea
)

from gui.ui.tools_box_scroll_widget import ToolsBoxScrollWidget

class SideBarWidget(QWidget):

    def __init__(self, parent=None, main_layout=None):
        super(SideBarWidget, self).__init__(parent)

        self.tools_box_widget = ToolsBoxScrollWidget(parent)

        # self.tools_box_widget.hide()

        self.parent = parent

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

        main_layout.addWidget(self.tools_box_widget)

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

    def __tools_menu_button__(self):

        button = QPushButton("Tools Box")
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

        def create_tool_box_widget(tools_box_widget):
            if tools_box_widget.isHidden():
                tools_box_widget.show()
            # tools_box_widget = ToolsBoxScrollWidget(parent)

            # main_layout.addWidget(tools_box_widget)

            # tools_box_widget.hide()

        button.clicked.connect(partial(create_tool_box_widget, self.tools_box_widget))

        return button

    @staticmethod
    def __notification_menu_button__():
        button = QPushButton("Notifiy Box")
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
        button = QPushButton("Reports")
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
        button = QPushButton("HackBox")
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
        button = QPushButton("Brain")
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
        button = QPushButton("Black Store")
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
        button = QPushButton("Setting")
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
