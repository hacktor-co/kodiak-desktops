"""
    - Created on Nov 1/2019 - hacktorco
    - All rights reserved for hacktor team

    - scroll bar for tools box widget to show all tool headers
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox
)

from gui.common.styles.settingpages.setting_box_scroll_widget_style import *
from gui.ui.toolsboxpage.tools_box_holder_widget import ToolsBoxHolderWidget
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from common.constants.consts import (
    HYPER_GUI_ASSET_PATH
)
from common.utils.os_helper import get_os_info


class SettingBoxScrollWidget(QWidget):
    def __init__(self, parent=None, setting_page_holder=None):
        super(SettingBoxScrollWidget, self).__init__(parent)

        if self.isHidden() is not True:
            self.setting_page_holder = setting_page_holder

            self.setting_page_holder.set_hide(False)
            self.setting_page_holder.create_widget("General")

            self.setLayoutDirection(Qt.RightToLeft)

            if get_os_info()["os"] == "Windows":
                self.setStyleSheet(main_widget_style_setting_box_windows)
            else:
                self.setStyleSheet(main_widget_style_setting_box)

            form_layout = QFormLayout()
            form_layout.setAlignment(Qt.AlignBottom)

            group_box = QGroupBox()
            group_box.setAccessibleName(setting_groupbox_style[0])
            group_box.setStyleSheet(setting_groupbox_style[1])
            group_box.setContentsMargins(0, 0, 0, 0)

            form_layout.addRow(self.__button_general_setting__())
            form_layout.addRow(self.__button_services_setting__())
            form_layout.addRow(self.__button_me_setting__())

            group_box.setLayout(form_layout)

            scroll_area = QScrollArea()
            scroll_area.setAccessibleName(setting_scroll_area_style[0])
            scroll_area.setStyleSheet(setting_scroll_area_style[1])
            scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll_area.setWidget(group_box)

            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addStretch()

            layout.addWidget(scroll_area)

    def __button_general_setting__(self):
        button = QPushButton()
        button.setAccessibleName(setting_category_btn_style[0])
        button.setStyleSheet(setting_category_btn_style[1])
        button.setContentsMargins(0, 0, 0, 0)

        button_icon = QIcon(HYPER_GUI_ASSET_PATH + "/general_setting_btn_icon.svg")
        button.setIconSize(QSize(70, 70))
        button.setIcon(button_icon)

        def show_general_setting_menus(parent):
            parent.setting_page_holder.set_hide(False)
            parent.setting_page_holder.create_widget("General")

        button.clicked.connect(partial(show_general_setting_menus, self))

        return button

    def __button_services_setting__(self):
        button = QPushButton()
        button.setAccessibleName(setting_category_btn_style[0])
        button.setStyleSheet(setting_category_btn_style[1])
        button.setContentsMargins(0, 0, 0, 0)

        button_icon = QIcon(HYPER_GUI_ASSET_PATH + "/services_setting_btn_icon.svg")
        button.setIconSize(QSize(70, 70))
        button.setIcon(button_icon)

        def show_services_setting_menus(parent):
            parent.setting_page_holder.set_hide(False)
            parent.setting_page_holder.create_widget("services")

        button.clicked.connect(partial(show_services_setting_menus, self))

        return button

    def __button_me_setting__(self):
        button = QPushButton()
        button.setAccessibleName(setting_category_btn_style[0])
        button.setStyleSheet(setting_category_btn_style[1])
        button.setContentsMargins(0, 0, 0, 0)

        button_icon = QIcon(HYPER_GUI_ASSET_PATH + "/me_setting_btn_icon.svg")
        button.setIconSize(QSize(70, 70))
        button.setIcon(button_icon)

        def show_me_setting_menus(parent):
            parent.setting_page_holder.set_hide(True)
            parent.setting_page_holder.create_widget("me")

        button.clicked.connect(partial(show_me_setting_menus, self))

        return button

    def set_hide(self, hide):
        if hide:
            self.hide()
        else:
            self.show()
