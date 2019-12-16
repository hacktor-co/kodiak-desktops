"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
)

class MainWindow(QMainWindow):

    def init(self, parent):
        super().__init__()
        self.setLayoutDirection(Qt.RightToLeft)

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            # 1080 -> width of window
            # 800  -> height og window
            int((screen_size.width() - 1000) / 2),
            int((screen_size.height() - 800) / 2),
            0, 0
        )  # set the main window to center of screen

    def execute_app(self, parent=None):
        self.init(parent)
        self.show()
