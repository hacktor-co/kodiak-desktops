"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QHBoxLayout, QWidget, QApplication
)

from .gui.main_window_handler import MainWindowHandler
from .gui.styles.gui_handler_styles import *


class MainWindow(QMainWindow):

    def init(self, parent):
        super().__init__()
        self.setAccessibleName("QMainWindowStyle")
        self.setWindowTitle("Directory Finder")
        self.setStyleSheet(main_window_style)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setContentsMargins(0, 0, 0, 0)

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            # 1080 -> width of window
            # 800  -> height og window
            int((screen_size.width() - 1080) / 2),
            int((screen_size.height() - 800) / 2),
            0, 0
        )  # set the main window to center of screen

        self.__add_widgets__()

    def __add_widgets__(self):
        widget = QWidget(self)

        main_layout = QHBoxLayout(widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addStretch()

        mainwindow_handler = MainWindowHandler(self, parent_layout=main_layout)

        main_layout.addWidget(mainwindow_handler)

        self.setCentralWidget(widget)

    def execute_app(self, parent=None):
        self.init(parent)

        self.show()
