"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QHBoxLayout, QWidget
)

from .gui.windows.main_window_handler import MainWindowHandler
from .gui.styles.main_window_styles import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet(main_window_style)
        self.setWindowTitle("Directory finder")
        self.setLayoutDirection(Qt.LeftToRight)
        self.__add_widgets__()

    def __add_widgets__(self):
        widget = QWidget(self)

        main_layout = QHBoxLayout(widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addStretch()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)

        mainwindow_handler = MainWindowHandler(self, parent_layout=main_layout)

        main_layout.addWidget(mainwindow_handler)

        self.setCentralWidget(widget)

    def execute_app(self, parent=None):
        self.show()
