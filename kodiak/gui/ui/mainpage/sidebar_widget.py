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
from incommon.constants.consts import DEFINE_FIRST_TOOLBOX_PACKAGE_TO_SHOW
from incommon.utils.os_helper import get_os_info
from gui.ui.settingpages.setting_box_scroll_widget import SettingBoxScrollWidget
from gui.ui.settingpages.setting_page_menu_holder_widget import SettingPageMenuHolderWidget


class SideBarWidget(QWidget):

    def __init__(self, parent=None, main_layout=None):
        super(SideBarWidget, self).__init__(parent)

        self.main_layout = main_layout
        # init all boxes layout
        self.parent = parent

        self.tools_box_holder_widget = ToolsBoxHolderWidget(parent, boxname=DEFINE_FIRST_TOOLBOX_PACKAGE_TO_SHOW)
        self.tools_box_scroll_widget = ToolsBoxScrollWidget(parent, toolbox_holder=self.tools_box_holder_widget)

        self.setting_page_holder_widget = SettingPageMenuHolderWidget(parent)
        self.setting_box_scroll_widget = SettingBoxScrollWidget(parent, setting_page_holder=self.setting_page_holder_widget)
        self.setting_page_holder_widget.set_hide(True)
        self.setting_box_scroll_widget.set_hide(True)
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

        self.main_layout.addWidget(self.setting_page_holder_widget)
        self.main_layout.addWidget(self.setting_box_scroll_widget)
        self.main_layout.addWidget(self.tools_box_holder_widget)
        self.main_layout.addWidget(self.tools_box_scroll_widget)

    @staticmethod
    def __icon_holder_frame__():

        icon_holder = QLabel()

        image = QPixmap('./gui/assets/kodiak_holder_icon.svg')

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

        self.button_toolbox_page = QPushButton()
        self.button_toolbox_page.setIcon(QIcon('./gui/assets/tools_img_icon.svg'))
        self.button_toolbox_page.setIconSize(QSize(70, 70))
        self.button_toolbox_page.setAccessibleName(selected_button[0])

        if get_os_info()["os"] == "Windows":
            self.button_toolbox_page.setStyleSheet(selected_button_windows[1])
        else:
            self.button_toolbox_page.setStyleSheet(selected_button[1])

        self.button_toolbox_page.setObjectName("btn_toolbox_sidebar")
        self.button_toolbox_page.clicked.connect(
            partial(self.set_style_onselected_button, self.button_toolbox_page.objectName())
        )

        return self.button_toolbox_page

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

        def create_tool_box_widget():
            pass

        button.clicked.connect(partial(create_tool_box_widget))

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

        def create_tool_box_widget():
            pass

        button.clicked.connect(partial(create_tool_box_widget))

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

        def create_tool_box_widget():
            print("report")

        button.clicked.connect(partial(create_tool_box_widget))

        return button

    def __setting_menu_button__(self):
        self.button_setting_page = QPushButton()
        self.button_setting_page.setAccessibleName(not_selected_button[0])
        self.button_setting_page.setIcon(QIcon('./gui/assets/setting_img_fade_icon.svg'))
        self.button_setting_page.setIconSize(QSize(70, 70))

        if get_os_info()["os"] == "Windows":
            self.button_setting_page.setStyleSheet(not_selected_button_windows[1])
        else:
            self.button_setting_page.setStyleSheet(not_selected_button[1])

        self.button_setting_page.setObjectName("btn_setting_sidebar")
        self.button_setting_page.clicked.connect(
            partial(self.set_style_onselected_button, self.button_setting_page.objectName())
        )

        return self.button_setting_page

    def set_style_onselected_button(self, button_name):
        if button_name == "btn_setting_sidebar":
            self.tools_box_scroll_widget.set_hide(True)
            self.tools_box_holder_widget.set_hide(True)

            self.setting_page_holder_widget.set_hide(False)
            self.setting_box_scroll_widget.set_hide(False)

            if get_os_info()["os"] == "Windows":
                self.button_setting_page.setAccessibleName(selected_button[0])
                self.button_setting_page.setStyleSheet(selected_button_windows[1])

                self.button_toolbox_page.setAccessibleName(not_selected_button[0])
                self.button_toolbox_page.setStyleSheet(not_selected_button_windows[1])

            else:
                self.button_setting_page.setAccessibleName(selected_button[0])
                self.button_setting_page.setStyleSheet(selected_button[1])

                self.button_toolbox_page.setAccessibleName(not_selected_button[0])
                self.button_toolbox_page.setStyleSheet(not_selected_button[1])

            self.button_setting_page.setIcon(QIcon('./gui/assets/setting_img_icon.svg'))
            self.button_setting_page.setIconSize(QSize(70, 70))

            # set other icon to fade
            self.button_toolbox_page.setIcon(QIcon('./gui/assets/tools_img_fade_icon.svg'))
            self.button_toolbox_page.setIconSize(QSize(70, 70))

        elif button_name == "btn_toolbox_sidebar":
            self.setting_box_scroll_widget.set_hide(True)
            self.setting_page_holder_widget.set_hide(True)

            self.tools_box_scroll_widget.set_hide(False)
            self.tools_box_holder_widget.set_hide(False)

            if get_os_info()["os"] == "Windows":
                self.button_toolbox_page.setAccessibleName(selected_button[0])
                self.button_toolbox_page.setStyleSheet(selected_button_windows[1])

                self.button_setting_page.setAccessibleName(not_selected_button[0])
                self.button_setting_page.setStyleSheet(not_selected_button_windows[1])

            else:
                self.button_toolbox_page.setAccessibleName(selected_button[0])
                self.button_toolbox_page.setStyleSheet(selected_button[1])

                self.button_setting_page.setAccessibleName(not_selected_button[0])
                self.button_setting_page.setStyleSheet(not_selected_button[1])

            self.button_toolbox_page.setIcon(QIcon('./gui/assets/tools_img_icon.svg'))
            self.button_toolbox_page.setIconSize(QSize(70, 70))

            # set other icon to fade
            self.button_setting_page.setIcon(QIcon('./gui/assets/setting_img_fade_icon.svg'))
            self.button_setting_page.setIconSize(QSize(70, 70))
