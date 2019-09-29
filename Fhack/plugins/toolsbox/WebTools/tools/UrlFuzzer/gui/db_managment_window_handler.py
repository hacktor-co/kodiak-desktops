
from PyQt5.QtWidgets import (
    QDialog
)

class MainWindow(QDialog):

    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet("""
            min-width: 800px;
            max-width: 800px;
            background-color: #1f1f1f;
            min-height: 600px;
            max-height: 600px;
        """)

        self.exec()

        # AdminFinderModel.create(path="admin").save()
        # AdminFinderModel.create(path="admin").save()
        # DataBaseHelper().close()
