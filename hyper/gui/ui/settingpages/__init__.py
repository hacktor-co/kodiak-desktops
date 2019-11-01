"""
    - Created on Nov 1/2019 - hacktorco
    - All rights reserved for hacktor team

    - scroll bar for setting box widget to show all title menu of settings
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
    DEFINE_PLUGIN_TOOLSBOX_PATH, DEFINE_PLUGIN_TOOLSBOX_ASSET_PATH
)
from common.utils.os_helper import get_os_info


class SettingBoxScrollWidget(QWidget):

    def __init__(self, parent=None, settingbox_holder=None):
        super(SettingBoxScrollWidget, self).__init__(parent)
        # self.settingbox_holder = settingbox_holder
        if self.isHidden() is not True:

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

            # button = QPushButton("General")
            # button.setAccessibleName(setting_category_btn_style[0])
            # button.setStyleSheet(setting_category_btn_style[1])
            # button.setContentsMargins(0, 0, 0, 0)

            # def selected_tools_box_widget(boxname, toolbox_holder_widgets):
            #     toolbox_holder_widgets.create_widget(boxname)
            #
            # asset_path = (
            #         GET_CWD + DEFINE_PLUGIN_TOOLSBOX_PATH + '/' +
            #         tool_category + DEFINE_PLUGIN_TOOLSBOX_ASSET_PATH + "/"
            # )
            #
            # button_icon = QIcon(asset_path + tool_category)  # set icon's of all buttons that exist in toolboxs
            # button.setIconSize(QSize(70, 70))
            # button.setIcon(button_icon)

            # button.clicked.connect(partial(selected_tools_box_widget, tool_category, self.toolbox_holder_widget))

            # form_layout.addRow(button)

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

    def set_hide(self, hide):
        if hide:
            self.hide()
        else:
            self.show()