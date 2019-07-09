#!/usr/bin/python3
"""
    - Created on jun 5/2019 - hacktorco
    - All rights reserved for hacktor team

    - This package handle main window of application
"""


from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QStackedWidget,
    QSizePolicy
)

from gui.ui.sidebar_widget import SideBarWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("FHack")

        self.central_widget = QStackedWidget()

        self.setCentralWidget(self.central_widget)

        self.__add_widgets__()
        self.__init_ui__()

    def __add_widgets__(self):

        sidebar_widget = SideBarWidget(self)
        self.central_widget.addWidget(sidebar_widget)

    def __init_ui__(self):
        self.setStyleSheet(
            """
                background-color: #1b222c;
                min-width: 1150px;
                max-width: 1150px;
                min-height: 790px;
                max-height: 790px;
            """
        )

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            int((screen_size.width() - 800) / 2),
            int((screen_size.height() - 600) / 2),
            0, 0
        )  # set the main window to center of screen

        self.show()
