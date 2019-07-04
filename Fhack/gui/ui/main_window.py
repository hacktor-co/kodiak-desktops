
from PyQt5.QtWidgets import (
    QWidget, QApplication
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FHack")

        screen_size = QApplication.desktop().geometry()

        self.setGeometry(
            int((screen_size.width() - 800) / 2),
            int((screen_size.height() - 600) / 2),
            0, 0
        ) # set the main window to center of screen

        self.setStyleSheet(
            """
                background-color: #fff;
                min-width: 800px;
                max-width: 800px;
                min-height: 600px;
                max-height: 600px;
            """
        )

        self.__init_ui__()

    def __init_ui__(self):
        self.show()
