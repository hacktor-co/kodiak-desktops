
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QListWidget
)
from PyQt5.QtCore import Qt


class MainWindowHandler(QWidget):
    def __init__(self, parent=None, parent_layout=None):
        super().__init__()
        self.__init_ui__()

    @staticmethod
    def __add_controls__(org_layout):
        tool_bar_layout = QHBoxLayout()
        tool_bar_layout.addStretch()
        tool_bar_layout.setContentsMargins(0, 0, 0, 0)
        tool_bar_layout.setAlignment(Qt.AlignTop)

        tableWidget = QTableWidget()
        tableWidget.setAccessibleName("tableViewResult")
        tableWidget.setStyleSheet(
            """
                [accessibleName="tableViewResult"] {
                    background-color: #1f1f1f;
                    min-height: 400px;
                    min-width: 1080px;
                    max-width: 1080px;
                    max-height: 400px;
                }
            """
        )
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(2)
        tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        tableWidget.setLayoutDirection(Qt.LeftToRight)
        tool_bar_layout.addWidget(tableWidget)

        org_layout.addLayout(tool_bar_layout)

    def __init_ui__(self):
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.__add_controls__(main_layout)

        self.setLayout(main_layout)
