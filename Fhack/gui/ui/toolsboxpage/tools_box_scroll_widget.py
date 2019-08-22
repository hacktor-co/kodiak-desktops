"""
    - Created on jul 13/2019 - hacktorco
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

from gui.common.styles.toolsboxpage.tools_box_scroll_widget_styles import *
from gui.ui.toolsboxpage.tools_box_holder_widget import ToolsBoxHolderWidget
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from common.constants.consts import (
    DEFINE_PLUGIN_TOOLSBOX_PATH, DEFINE_PLUGIN_TOOLSBOX_ASSET_PATH
)


class ToolsBoxScrollWidget(QWidget):
    def __init__(self, parent=None, toolbox_holder=None):
        super(ToolsBoxScrollWidget, self).__init__(parent)

        self.toolbox_holder_widget = toolbox_holder

        if self.isHidden() is not True:
            self.setStyleSheet(main_widget_style)

            form_layout = QFormLayout()
            form_layout.setAlignment(Qt.AlignLeft)

            group_box = QGroupBox()
            group_box.setStyleSheet(group_box_style)
            group_box.setContentsMargins(0, 0, 0, 0)

            # other programmer that want's to write plugin on ToolBox package must create assets on each directory
            # and set image with svg format and same name as ToolBox's package
            for tool_category in get_all_directory(GET_CWD + DEFINE_PLUGIN_TOOLSBOX_PATH, 0):
                button = QPushButton()
                button.setStyleSheet(tool_category_btn_style)
                button.setContentsMargins(0, 0, 0, 0)

                def selected_tools_box_widget(boxname, toolbox_holder_widgets):
                    toolbox_holder_widgets.create_widget(boxname)

                asset_path = (
                        GET_CWD + DEFINE_PLUGIN_TOOLSBOX_PATH + '/' +
                        tool_category + DEFINE_PLUGIN_TOOLSBOX_ASSET_PATH + "/"
                )

                button_icon = QIcon(asset_path + tool_category)  # set icon's of all buttons that exist in toolboxs
                button.setIconSize(QSize(70, 70))
                button.setIcon(button_icon)

                button.clicked.connect(partial(selected_tools_box_widget, tool_category, self.toolbox_holder_widget))

                form_layout.addRow(button)

            group_box.setLayout(form_layout)

            scroll_area = QScrollArea()
            scroll_area.setStyleSheet(scroll_area_style)
            scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            scroll_area.setWidget(group_box)

            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addStretch()

            layout.addWidget(scroll_area)
