"""
    - Created on Nov 4/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package handle general page setting controls and widgets
        on this page hyper will add plugin that user download it from
        third paraty programmer.
"""

from functools import partial
import zipfile
from json import loads as json_load

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QFrame, QTextEdit,
    QPushButton, QFormLayout, QVBoxLayout, QFileDialog,
    QProgressBar
)

from common.constants.consts import (
    HYPER_GUI_ASSET_PATH
)
from gui.common.styles.settingpages.general_setting_plugin_manager_style import *


class PluginManagerGeneralSetting:
    def __init__(self, parent=None):
        self.parent = parent

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

        self.__add_items__()
        self.__add_plugin_content_info_section__()
        self.__add_description_section__()
        self.__add_submit_section__()

    def __btn_extract_plugin_clicked__(self):
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            with zip_file.open(self.zip_name + "/wire.json", "r") as wire_file:
                wire = json_load(wire_file.read())
                zip_file.extractall("./plugins/toolsbox/" + str(wire["category"]) + "/tools/")
        del self.zip_name, self.file_name

    def __get_plugin_from_user__(self, file_path, zip_name):
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            with zip_file.open(zip_name + "/wire.json", "r") as wire_file:
                wire = json_load(wire_file.read())
                self.category_label.setText("Category: " + str(wire["category"]))
                self.version_label.setText("Version: " + str(wire["version"]))
                self.plugin_author.setText("Author: " + str(wire["author"]["name"]))
                self.plugin_size.setText("Size: " + str(465))
                self.plugin_name.setText("Name: " + str(wire["name"]))
                self.text_line.setText(str(wire["description"]))

    def __clicked_btn_add_plugin__(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file_name, _ = QFileDialog.getOpenFileName(
            self.parent, "Select plugin", "",
            "All zip files (*.zip)", options=options
        )

        if self.file_name:
            if self.file_name.find("/") != -1:
                self.zip_name = self.file_name.split("/")[len(self.file_name.split("/")) - 1].split(".zip")[0]
            else:
                self.zip_name = self.file_name.split("\\")[len(self.file_name.split("\\")) - 1].split(".zip")[0]

            self.__get_plugin_from_user__(self.file_name, self.zip_name)

    def __add_items__(self):

        h_box_layout = QHBoxLayout()
        h_box_layout.addStretch()
        h_box_layout.setContentsMargins(20, 20, 20, 20)

        button_addplugin = QPushButton()
        button_addplugin.setAccessibleName(plugin_manager_general_setting_btn_add_plugin_style[0])
        button_addplugin.setStyleSheet(plugin_manager_general_setting_btn_add_plugin_style[1])
        button_icon = QIcon(HYPER_GUI_ASSET_PATH + "/add_plugin_general_setting_icon.svg")
        button_addplugin.setIconSize(QSize(70, 70))
        button_addplugin.setIcon(button_icon)
        button_addplugin.clicked.connect(partial(self.__clicked_btn_add_plugin__))

        h_box_layout.addWidget(button_addplugin)

        v_plugin_info_layout = QVBoxLayout()
        v_plugin_info_layout.addStretch()
        v_plugin_info_layout.setContentsMargins(0, 0, 0, 0)

        self.plugin_name = QLabel("Name")
        self.plugin_name.setContentsMargins(0, 0, 0, 0)
        self.plugin_name.setAccessibleName(plugin_manager_general_labels_style[0])
        self.plugin_name.setStyleSheet(plugin_manager_general_labels_style[1])

        v_plugin_info_layout.addWidget(self.plugin_name)

        self.plugin_author = QLabel("Author")
        self.plugin_author.setContentsMargins(0, 0, 0, 0)
        self.plugin_author.setAccessibleName(plugin_manager_general_labels_style[0])
        self.plugin_author.setStyleSheet(plugin_manager_general_labels_style[1])

        v_plugin_info_layout.addWidget(self.plugin_author)

        self.category_label = QLabel("Category")
        self.category_label.setContentsMargins(0, 0, 0, 0)
        self.category_label.setAccessibleName(plugin_manager_general_labels_style[0])
        self.category_label.setStyleSheet(plugin_manager_general_labels_style[1])

        v_plugin_info_layout.addWidget(self.category_label)

        h_box_layout.addLayout(v_plugin_info_layout)

        self.layout.addLayout(h_box_layout)

    def __add_plugin_content_info_section__(self):

        h_box_layout = QHBoxLayout()
        h_box_layout.setContentsMargins(20, 0, 45, 20)
        h_box_layout.addStretch()
        h_box_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.plugin_size = QLabel("Size")
        self.plugin_size.setContentsMargins(0, 0, 0, 0)
        self.plugin_size.setAccessibleName(plugin_content_info_section_label_style[0])
        self.plugin_size.setStyleSheet(plugin_content_info_section_label_style[1])

        h_box_layout.addWidget(self.plugin_size)

        self.version_label = QLabel("Version")
        self.version_label.setContentsMargins(0, 0, 0, 0)
        self.version_label.setAccessibleName(plugin_content_info_section_label_style[0])
        self.version_label.setStyleSheet(plugin_content_info_section_label_style[1])

        h_box_layout.addWidget(self.version_label)

        self.layout.addLayout(h_box_layout)

    def __add_description_section__(self):
        h_box_layout = QHBoxLayout()
        h_box_layout.setContentsMargins(20, 0, 20, 20)
        h_box_layout.addStretch()
        h_box_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.text_line = QTextEdit()
        self.text_line.setReadOnly(True)
        self.text_line.setAccessibleName(text_description_style[0])
        self.text_line.setStyleSheet(text_description_style[1])

        h_box_layout.addWidget(self.text_line)

        self.layout.addLayout(h_box_layout)

    def __add_submit_section__(self):
        h_box_layout = QHBoxLayout()
        h_box_layout.setContentsMargins(20, 0, 20, 20)
        h_box_layout.addStretch()
        h_box_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        submit_button = QPushButton("Add To Hyper")
        submit_button.setAccessibleName(btn_submit_plugin_style[0])
        submit_button.setStyleSheet(btn_submit_plugin_style[1])
        submit_button.clicked.connect(partial(self.__btn_extract_plugin_clicked__))

        h_box_layout.addWidget(submit_button)

        progress_bar = QProgressBar()
        progress_bar.setAccessibleName(progress_bar_add_plugin_setting_style[0])
        progress_bar.setStyleSheet(progress_bar_add_plugin_setting_style[1])

        h_box_layout.addWidget(progress_bar)

        self.layout.addLayout(h_box_layout)

    def get_layout(self):
        return self.layout
