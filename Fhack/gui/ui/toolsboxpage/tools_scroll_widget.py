"""
    - Created on jul 31/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package get all tools in toolbox from parent class then
        show it with scroll widget
"""

from functools import partial
from importlib import import_module
import json
from os import path

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox
)

from gui.common.styles.toolsboxpage.tools_scroll_widget_styles import (
    button_tool_style, scroll_area_style, group_box_style
)
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

    @staticmethod
    def __get_plugin__(box_name, tool_name):
        """ get plugin from tools box section
        :param box_name: tool box name
        :param tool_name: tool name
        :return: entry point of plugin
        """
        plugin_module_path = (
                "plugins.toolsbox" + "." +
                box_name + "." + "tools" + "." + tool_name + ".gui_handler"
        )

        plugin_module = import_module(plugin_module_path, ".")
        plugin = plugin_module.MainWindow()

        return plugin.execute_app

    @staticmethod
    def __get_wire__(box_name: str, tool: str) -> str:
        return "./plugins/toolsbox/" + box_name + "/tools/" + tool + "/wire.json"

    def __set_specific_style__(self, box_name: str, tool: str) -> str:
        with open(self.__get_wire__(box_name, tool), 'r') as file:
            button_style = button_tool_style
            wire = json.load(file)
            for item in wire["assets"]:
                for _ in wire["assets"][item]:
                    button_style += _ + ":" + wire["assets"][item][_] + ";"
            return button_style

    @staticmethod
    def __set_tool_icon__(box_name: str, tool: str, button):
        # set icon's of all buttons that exist in assets of tool
        if path.exists("./plugins/toolsbox/" + box_name + "/tools/" + tool + "/assets/mainico.svg"):
            button_icon = QIcon("./plugins/toolsbox/" + box_name + "/tools/" + tool + "/assets/mainico.svg")
            button.setIconSize(QSize(70, 70))
            button.setIcon(button_icon)
        else:
            button.setText(tool)

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

            for tool in list_tools_path:
                button = QPushButton()

                self.__set_tool_icon__(box_name, tool, button)

                button.setStyleSheet(self.__set_specific_style__(box_name, tool))
                button.clicked.connect(
                    partial(
                        self.__get_plugin__(
                            box_name, tool
                        ), self
                    )
                )

                layout.addWidget(button)
                if tool_counter % 4 == 0:
                    layout_v.addLayout(layout)

                    layout = QHBoxLayout()
                    layout.setContentsMargins(5, 0, 5, 0)
                    layout.addStretch()

                    remind_list.append(tool)

                tool_counter += 1

            # draw all remind item in list
            for tool in remind_list:
                button = QPushButton()

                self.__set_tool_icon__(box_name, tool, button)

                button.setStyleSheet(self.__set_specific_style__(box_name, tool))
                button.clicked.connect(
                    partial(
                        self.__get_plugin__(
                            box_name, tool
                        ), self
                    )
                )
                layout.addWidget(button)

            layout_v.addLayout(layout)
        else:
            # draw tools if toolsbox item is < 4
            for tool in list_tools_path:
                button = QPushButton()

                self.__set_tool_icon__(box_name, tool, button)

                button.setStyleSheet(self.__set_specific_style__(box_name, tool))
                button.clicked.connect(
                    partial(
                        self.__get_plugin__(
                            box_name, tool
                        ), self
                    )
                )
                layout.addWidget(button)

            layout_v.addLayout(layout)

        group_box.setLayout(layout_v)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet(scroll_area_style)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setWidget(group_box)

        top_bar = TopToolBar(self, location_path=box_name)

        self.parent_layout.layout.addWidget(top_bar)

        self.parent_layout.layout.addWidget(scroll_area)  # parent layout is => QVBoxLayout
