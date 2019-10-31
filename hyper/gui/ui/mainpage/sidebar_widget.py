#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - side bar menu ui's code
"""

from functools import partial

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QPushButton, QFrame, QScrollArea
)

from gui.common.styles.mainpage.sidebar_widget_styles import *
from gui.ui.toolsboxpage.tools_box_scroll_widget import ToolsBoxScrollWidget
from gui.ui.toolsboxpage.tools_box_holder_widget import ToolsBoxHolderWidget
from common.constants.consts import DEFINE_FIRST_TOOLBOX_PACKAGE_TO_SHOW
from common.utils.os_helper import get_os_info


class SideBarWidget(QWidget):

    def __init__(self, parent=None, main_layout=None):
        super(SideBarWidget, self).__init__(parent)

        # init all boxes layout
        self.tools_box_holder_widget = ToolsBoxHolderWidget(parent, boxname=DEFINE_FIRST_TOOLBOX_PACKAGE_TO_SHOW)
        self.tools_box_scroll_widget = ToolsBoxScrollWidget(parent, toolbox_holder=self.tools_box_holder_widget)
        # end
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addStretch()
        sidebar_layout.addSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)

        self.setAccessibleName(main_widget_style[0])
        self.setStyleSheet(main_widget_style[1])

        sidebar_layout.addWidget(self.__icon_holder_frame__())
        sidebar_layout.addWidget(self.__setting_menu_button__())
        sidebar_layout.addWidget(self.__tools_menu_button__())
        sidebar_layout.addWidget(self.__report_menu_button__())
        sidebar_layout.addWidget(self.__blackbox_button__())
        sidebar_layout.addWidget(self.__brain_button__())

        self.setLayout(sidebar_layout)

        main_layout.addWidget(self.tools_box_holder_widget)
        main_layout.addWidget(self.tools_box_scroll_widget)

    @staticmethod
    def __icon_holder_frame__():

        icon_holder = QLabel()

        image = QPixmap('./gui/assets/fhack_main_ico.svg')

        image.scaled(10, 10)

        icon_holder.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        icon_holder.setPixmap(image)

        icon_holder.setAccessibleName(icon_holder_frame_style[0])
        if get_os_info()["os"] == "Windows":
            icon_holder.setStyleSheet(icon_holder_frame_style_windows[1])
        else:
            icon_holder.setStyleSheet(icon_holder_frame_style[1])

        icon_holder.setContentsMargins(0, 0, 0, 0)

        return icon_holder

    def __tools_menu_button__(self):

        button = QPushButton()
        button.setIcon(QIcon('./gui/assets/tools_img_icon.svg'))
        button.setIconSize(QSize(70, 70))
        button.setAccessibleName(selected_button[0])

        if get_os_info()["os"] == "Windows":
            button.setStyleSheet(selected_button_windows[1])
        else:
            button.setStyleSheet(selected_button[1])

        def create_tool_box_widget(tools_box_widget):
            if tools_box_widget.isHidden():
                tools_box_widget.show()

        button.clicked.connect(partial(create_tool_box_widget, self.tools_box_scroll_widget))

        return button

    @staticmethod
    def __brain_button__():
        button = QPushButton()
        button.setAccessibleName(not_selected_button[0])

        if get_os_info()["os"] == "Windows":
            button.setStyleSheet(not_selected_button_windows[1])
        else:
            button.setStyleSheet(not_selected_button[1])

        button.setIcon(QIcon('./gui/assets/brain_img_fade_icon.svg'))
        button.setIconSize(QSize(70, 70))

        def create_tool_box_widget():  # tools_box_widget):
            # if tools_box_widget.isHidden():
            #     tools_box_widget.show()
            print("brain")

        button.clicked.connect(partial(create_tool_box_widget))  # , self.tools_box_scroll_widget))

        return button

    @staticmethod
    def __blackbox_button__():
        button = QPushButton()
        button.setAccessibleName(not_selected_button[0])

        if get_os_info()["os"] == "Windows":
            button.setStyleSheet(not_selected_button_windows[1])
        else:
            button.setStyleSheet(not_selected_button[1])

        button.setIcon(QIcon('./gui/assets/black_box_img_fade_icon.svg'))
        button.setIconSize(QSize(70, 70))

        def create_tool_box_widget():  # tools_box_widget):
            # if tools_box_widget.isHidden():
            #     tools_box_widget.show()
            print("black box")

        button.clicked.connect(partial(create_tool_box_widget))  # , self.tools_box_scroll_widget))

        return button

    @staticmethod
    def __report_menu_button__():
        button = QPushButton()
        button.setAccessibleName(not_selected_button[0])

        if get_os_info()["os"] == "Windows":
            button.setStyleSheet(not_selected_button_windows[1])
        else:
            button.setStyleSheet(not_selected_button[1])

        button.setIcon(QIcon('./gui/assets/report_img_fade_icon.svg'))
        button.setIconSize(QSize(70, 70))

        def create_tool_box_widget():#tools_box_widget):
            # if tools_box_widget.isHidden():
            #     tools_box_widget.show()
            print("report")

        button.clicked.connect(partial(create_tool_box_widget)) #, self.tools_box_scroll_widget))

        return button

    @staticmethod
    def __setting_menu_button__():
        button = QPushButton()
        button.setAccessibleName(not_selected_button[0])

        if get_os_info()["os"] == "Windows":
            button.setStyleSheet(not_selected_button_windows[1])
        else:
            button.setStyleSheet(not_selected_button[1])

        button.setIcon(QIcon('./gui/assets/setting_img_fade_icon.svg'))
        button.setIconSize(QSize(70, 70))

        def create_tool_box_widget():#tools_box_widget):
            # if tools_box_widget.isHidden():
            #     tools_box_widget.show()
            print("setting")

        button.clicked.connect(partial(create_tool_box_widget)) #, self.tools_box_scroll_widget))

        return button
