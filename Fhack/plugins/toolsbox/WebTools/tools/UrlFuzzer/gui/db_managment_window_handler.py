
from PyQt5.QtWidgets import (
    QMainWindow
)

class MainWindow(QMainWindow):

    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet("""
            min-width: 500px;
            max-width: 500px;
            min-height: 500px;
            max-height: 500px;
        """)

        self.show()

        # AdminFinderModel.create(path="admin").save()
        # AdminFinderModel.create(path="admin").save()
        # DataBaseHelper().close()
