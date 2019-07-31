#!/usr/bin/python3
"""
    - Created on jul 28/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package get all tools in toolbox from parent class then
        show it with scroll widget
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QHBoxLayout,
    QPushButton, QFormLayout, QGroupBox
)

from gui.common.styles.toolsboxpage.tools_box_scroll_widget_styles import *
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from common.constants.consts import (
    DEFINE_PLUGIN_TOOLSBOX_PATH, DEFINE_PLUGIN_TOOLSBOX_ASSET_PATH
)


class ToolsScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsScrollWidget, self).__init__(parent)

        self.parent_layout = parent

    def generate_widget(self, list_tools_path):
        print(list_tools_path)

        self.setStyleSheet(main_widget_style)

        group_box = QGroupBox()
        group_box.setStyleSheet(group_box_style)
        group_box.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout()
        layout.setContentsMargins(5, 0, 5, 0)
        layout.addStretch()

        layout_v = QVBoxLayout()
        layout_v.addStretch()

        for tool_category in range(1, 10):
            button = QPushButton("item")
            button.setStyleSheet("""
                    min-width: 200px;
                    max-width: 200px;
                    min-height: 200px;
                    max-height: 200px;
                    background-color: red;
                """)
            layout.addWidget(button)
            if tool_category % 4 == 0:
                layout_v.addLayout(layout)

                layout = QHBoxLayout()
                layout.setContentsMargins(5, 0, 5, 0)
                layout.addStretch()
            #
            # if tool_category % 3 == 0:
            #     print(tool_category)
            #     print("I am here")
            #
            #     layout = QHBoxLayout(self)
            #     layout.setContentsMargins(0, 0, 0, 0)
            #     layout.addStretch()

        group_box.setLayout(layout_v)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet(scroll_area_style)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setWidget(group_box)

        self.parent_layout.layout.addWidget(scroll_area)  # parent layout is => QVBoxLayout
