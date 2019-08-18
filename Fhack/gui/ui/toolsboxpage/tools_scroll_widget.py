#!/usr/bin/python3
"""
    - Created on jul 31/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package get all tools in toolbox from parent class then
        show it with scroll widget
"""

from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox
)

from gui.common.styles.toolsboxpage.tools_scroll_widget_styles import *
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from common.constants.consts import (
    DEFINE_PLUGIN_TOOLSBOX_PATH, DEFINE_PLUGIN_TOOLSBOX_ASSET_PATH
)
from gui.ui.components.custom_widgets.top_tool_bar import TopToolBar


class ToolsScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsScrollWidget, self).__init__(parent)

        self.parent_layout = parent

    def generate_widget(self, list_tools_path, box_name):

        group_box = QGroupBox()
        group_box.setStyleSheet(group_box_style)
        group_box.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout()
        layout.setContentsMargins(5, 0, 5, 0)
        layout.addStretch()

        layout_v = QVBoxLayout()
        layout_v.addStretch()

        # draw box foreach tool in toolbox plugin algorithem
        if len(list_tools_path) > 4:
            tool_counter = 1
            remind_list = list()

            for tool_category in list_tools_path:
                button = QPushButton(tool_category)

                button.setStyleSheet(button_tool_style)
                layout.addWidget(button)
                if tool_counter % 4 == 0:
                    layout_v.addLayout(layout)

                    layout = QHBoxLayout()
                    layout.setContentsMargins(5, 0, 5, 0)
                    layout.addStretch()

                    remind_list = tool_category[tool_counter - 1:]

                tool_counter += 1

            # draw all remind item in list
            for tool in remind_list:
                button = QPushButton(tool)
                button.setStyleSheet(button_tool_style)

                layout.addWidget(button)
            layout_v.addLayout(layout)
        else:

            from importlib import import_module

            for tool in list_tools_path:
                button = QPushButton(tool)
                button.setStyleSheet(button_tool_style)

                # plugin path
                plugin_module_path = (
                        "plugins.toolsbox" + "." +
                        box_name + "." + "tools" + "." + tool + ".gui_handler"
                )

                plugin_module = import_module(plugin_module_path, ".")
                plugin = plugin_module.MainWindow()

                button.clicked.connect(partial(plugin.execute_app, self))

                layout.addWidget(button)
            layout_v.addLayout(layout)

        group_box.setLayout(layout_v)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet(scroll_area_style)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setWidget(group_box)

        buttons = QPushButton("Button")
        buttons.setStyleSheet("""
            max-width: 100px;
            min-width: 100px;
            max-height: 100px;
            min-height: 100px;
        """)

        top_bar = TopToolBar(self)

        self.parent_layout.layout.addWidget(top_bar)

        self.parent_layout.layout.addWidget(scroll_area)  # parent layout is => QVBoxLayout
