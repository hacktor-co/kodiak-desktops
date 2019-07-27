#!/usr/bin/python3
"""
    - Created on jul 13/2019 - hacktorco
    - All rights reserved for hacktor team

    - scroll bar for tools box widget to show all tool headers
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox
)

from gui.common.styles.mainpage.tools_box_scroll_widget_styles import *
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from common.constants.consts import DEFINE_PLUGIN_TOOLSBOX_PATH


class ToolsBoxScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsBoxScrollWidget, self).__init__(parent)

        if self.isHidden() is not True:

            self.setStyleSheet(main_widget_style)

            form_layout = QFormLayout()
            form_layout.setAlignment(Qt.AlignLeft)

            group_box = QGroupBox()
            group_box.setStyleSheet("""
                border: none;
            """)
            group_box.setContentsMargins(0, 0, 0, 0)

            for tool_category in get_all_directory(GET_CWD + DEFINE_PLUGIN_TOOLSBOX_PATH):
                button = QPushButton(tool_category)
                button.setStyleSheet(tool_category_btn_style)
                form_layout.addRow(button)

            group_box.setLayout(form_layout)

            scroll = QScrollArea()
            scroll.setStyleSheet("""
                background-color: transparent;
            """)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            scroll.setWidget(group_box)

            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addStretch()

            layout.addWidget(scroll)
