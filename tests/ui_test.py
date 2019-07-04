import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FHack")
        self.setStyleSheet(
            """
                background-color: #fff;
                min-width: 640px;
                max-width: 640px;
                min-height: 800px;
                max-height: 800px;
            """
        )

        self.__init_ui__()

    def __init_ui__(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
