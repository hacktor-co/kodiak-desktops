#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - This package handle main window of application
"""

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QHBoxLayout,
    QSizePolicy, QWidget
)

from gui.common.styles.main_window_styles import *
from gui.ui.sidebar_widget import SideBarWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("FHack")

        self.__add_widgets__()
        self.__init_ui__()

    def __add_widgets__(self):

        widget = QWidget(self)

        main_layout = QHBoxLayout(widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addStretch()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        sidebar_widget = SideBarWidget(self, main_layout)

        main_layout.addWidget(sidebar_widget)

        self.setCentralWidget(widget)

    def __init_ui__(self):
        self.setStyleSheet(main_window_style)

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            int((screen_size.width() - 1150) / 2),
            int((screen_size.height() - 790) / 2),
            0, 0
        )  # set the main window to center of screen

        self.show()
