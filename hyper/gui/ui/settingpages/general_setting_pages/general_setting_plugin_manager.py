"""
    - Created on Nov 4/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package handle general page setting controls and widgets
"""

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QScrollArea, QFrame,
    QPushButton, QFormLayout, QGroupBox, QVBoxLayout,
)

from common.constants.consts import (
    HYPER_GUI_ASSET_PATH
)
from gui.common.styles.settingpages.general_setting_plugin_manager_style import *


class PluginManagerGeneralSetting:
    def __init__(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

        self.__add_items__()

    def __add_items__(self):

        h_box_layout = QHBoxLayout()
        h_box_layout.addStretch()
        h_box_layout.setContentsMargins(20, 20, 20, 600)

        button_addplugin = QPushButton()
        button_addplugin.setAccessibleName(plugin_manager_general_setting_btn_add_plugin_style[0])
        button_addplugin.setStyleSheet(plugin_manager_general_setting_btn_add_plugin_style[1])
        button_icon = QIcon(HYPER_GUI_ASSET_PATH + "/add_plugin_general_setting_icon.svg")
        button_addplugin.setIconSize(QSize(70, 70))
        button_addplugin.setIcon(button_icon)

        h_box_layout.addWidget(button_addplugin)

        v_plugin_info_layout = QVBoxLayout()
        v_plugin_info_layout.addStretch()
        v_plugin_info_layout.setContentsMargins(0, 0, 300, 30)

        plugin_name = QLabel("Name: ")
        plugin_name.setContentsMargins(0, 0, 0, 0)
        plugin_name.setAccessibleName(plugin_manager_general_labels_style[0])
        plugin_name.setStyleSheet(plugin_manager_general_labels_style[1])

        v_plugin_info_layout.addWidget(plugin_name)

        plugin_size = QLabel("Size: ")
        plugin_size.setContentsMargins(0, 0, 0, 0)
        plugin_size.setAccessibleName(plugin_manager_general_labels_style[0])
        plugin_size.setStyleSheet(plugin_manager_general_labels_style[1])

        v_plugin_info_layout.addWidget(plugin_size)

        plugin_author = QLabel("Author: ")
        plugin_author.setContentsMargins(0, 0, 0, 0)
        plugin_author.setAccessibleName(plugin_manager_general_labels_style[0])
        plugin_author.setStyleSheet(plugin_manager_general_labels_style[1])

        v_plugin_info_layout.addWidget(plugin_author)

        h_box_layout.addLayout(v_plugin_info_layout)

        self.layout.addLayout(h_box_layout)

    def get_layout(self):
        return self.layout
