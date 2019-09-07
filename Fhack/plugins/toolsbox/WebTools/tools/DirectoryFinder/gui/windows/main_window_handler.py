
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton
)

class MainWindowHandler(QWidget):
    def __init__(self, parent=None, parent_layout=None):
        super(MainWindowHandler, self).__init__(parent)
        self.__init_ui__()

    def __add_controls(self, org_layout):
        a = QPushButton("hello")
        a.setStyleSheet("""
            min-width: 100px;
            max-width: 100px;
            min-height: 100px;
            min-height: 100px;
        """)
        org_layout.addWidget(a)
        a = QPushButton("hello")
        a.setStyleSheet("""
            min-width: 100px;
            max-width: 100px;
            min-height: 100px;
            min-height: 100px;
        """)
        org_layout.addWidget(a)

    def __init_ui__(self):
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.__add_controls(main_layout)

        self.setLayout(main_layout)

