
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton,
    QAction, QMenu, QApplication, QHBoxLayout
)
from PyQt5.QtCore import Qt


class MainWindowHandler(QWidget):
    def __init__(self, parent=None, parent_layout=None):
        super(MainWindowHandler, self).__init__(parent)
        self.__init_ui__()

    @staticmethod
    def __add_controls__(org_layout):
        tool_bar_layout = QHBoxLayout()
        tool_bar_layout.addStretch()
        tool_bar_layout.setContentsMargins(0, 0, 0, 0)
        tool_bar_layout.setAlignment(Qt.AlignTop)

        button_new_workshop = QPushButton("1")
        button_new_workshop.setStyleSheet(
            """
                min-width: 100px;
                min-height: 100px;
                max-width: 100px;
                max-height: 100px;
                background-color: white;
                color: black;
            """
        )

        tool_bar_layout.addWidget(button_new_workshop)

        org_layout.addLayout(tool_bar_layout)

    def __init_ui__(self):
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignJustify)

        self.__add_controls__(main_layout)

        self.setLayout(main_layout)

