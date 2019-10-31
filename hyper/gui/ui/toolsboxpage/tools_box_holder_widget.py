"""
    - Created on jul 28/2019 - hacktorco
    - All rights reserved for hacktor team

    - all tools that tool category (tool box) contain's are here
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox
)

from common.constants.consts import (
    DEFINE_PLUGIN_TOOLS_PATH, DEFINE_PLUGIN_TOOLSBOX_PATH
)
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from gui.ui.toolsboxpage.tools_scroll_widget import ToolsScrollWidget
from gui.common.styles.toolsboxpage.tools_box_holder_widget_styles import *
from common.utils.os_helper import get_os_info


class ToolsBoxHolderWidget(QWidget):
    def __init__(self, parent=None, boxname: str = ""):
        super(ToolsBoxHolderWidget, self).__init__(parent)

        if get_os_info()["os"] == "Windows":
            self.setStyleSheet(main_style_windows)
        else:
            self.setStyleSheet(main_style)

        self.tools_scroll_widget = ToolsScrollWidget(parent=self)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

        self.create_widget(boxname)

    def create_widget(self, boxname):

        for i in reversed(range(self.layout.count())):
            if i == 0:
                break
            self.layout.itemAt(i).widget().deleteLater()

        tools_list_path = list()
        for tool in get_all_directory(
            GET_CWD + "/" + DEFINE_PLUGIN_TOOLSBOX_PATH + "/" +
            boxname + DEFINE_PLUGIN_TOOLS_PATH + "/", 0
        ):
            tools_list_path.append(tool)

        self.tools_scroll_widget.generate_widget(tools_list_path, box_name=boxname)
