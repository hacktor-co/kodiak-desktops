"""
    - Created on aug 22/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package is for component of current location in app
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout
)

from gui.common.styles.custom_widgets.app_location_holder_styles import *


class AppLocationHolder(QWidget):
    def __init__(self, parent=None, path: str = None):
        super(AppLocationHolder, self).__init__(parent)

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 5)
        layout_main.addStretch()
        self.setStyleSheet(main_style)

        location_holder = QLabel(path)
        location_holder.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        location_holder.setStyleSheet(label_location_holder)
        layout_main.addWidget(location_holder)

        self.setLayout(layout_main)
