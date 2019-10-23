"""
    - Created on jul 31/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package get all tools in toolbox from parent class then
        show it with scroll widget
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout
)

from gui.ui.components.custom_widgets.app_location_holder import AppLocationHolder
from gui.common.styles.custom_widgets.top_tool_bar_styles import *

class TopToolBar(QWidget):
    def __init__(self, parent=None, location_path: str = None):
        super(TopToolBar, self).__init__(parent)

        layout_main = QHBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.addStretch()
        self.setStyleSheet(main_style)

        # search button
        button = QPushButton()
        button.setStyleSheet(search_btn)
        button.setIcon(QIcon('./gui/assets/search_btn_icon.svg'))
        button.setIconSize(QSize(30, 30))
        layout_main.addWidget(button)
        # .......

        button = QPushButton()
        button.setStyleSheet(person_btn)
        button.setIcon(QIcon('./gui/assets/person_btn_icon.svg'))
        button.setIconSize(QSize(30, 30))
        layout_main.addWidget(button)

        app_location_holder = AppLocationHolder(self, path=location_path)
        layout_main.addWidget(app_location_holder)

        self.setLayout(layout_main)
