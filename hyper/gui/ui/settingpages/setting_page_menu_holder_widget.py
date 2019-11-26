"""
    - Created on Nov 2/2019 - hacktorco
    - All rights reserved for hacktor team

    - if user one item in menubar of setting then we create class that he/she selected
        this class work as factory for creating menu of setting items
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea,
    QPushButton, QFormLayout, QGroupBox
)

from incommon.constants.consts import (
    DEFINE_PLUGIN_TOOLS_PATH, DEFINE_PLUGIN_TOOLSBOX_PATH
)
from incommon.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from gui.ui.toolsboxpage.tools_scroll_widget import ToolsScrollWidget
from gui.common.styles.settingpages.setting_page_menu_holder_widget_style import *
from incommon.utils.os_helper import get_os_info


class SettingPageMenuHolderWidget(QWidget):
    def __init__(self, parent=None):
        super(SettingPageMenuHolderWidget, self).__init__(parent)

        self.parent = parent

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def create_widget(self, boxname):

        for i in reversed(range(self.layout.count())):
            if i == 0:
                break
            self.layout.itemAt(i).widget().deleteLater()

        if not self.isHidden():
            if get_os_info()["os"] == "Windows":
                self.setStyleSheet(main_style_windows)
            else:
                self.setStyleSheet(main_style)

            if boxname == "General":
                from gui.ui.settingpages.general_setting_pages.main_handler_widget_general_setting import \
                    MainHandlerWidgetGeneralSetting

                widget_add = MainHandlerWidgetGeneralSetting(self.parent)
                self.layout.addWidget(widget_add)

    def set_hide(self, hide):
        if hide:
            self.hide()
        else:
            self.show()
