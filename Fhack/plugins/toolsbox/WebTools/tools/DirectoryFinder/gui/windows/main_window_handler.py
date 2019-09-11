
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QListWidget
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
        #
        # listwidget = QListWidget()
        #
        # listwidget.setStyleSheet(
        #     """
        #         QListWidget {
        #             min-height: 400px;
        #             min-width: 360px;
        #             max-width: 360px;
        #             max-height: 400px;
        #             background-color: white;
        #         }
        #     """
        # )
        # listwidget.setLayoutDirection(Qt.LeftToRight)
        # listwidget.setMaximumWidth(360)
        # listwidget.setMinimumWidth(360)

        # for item in range(0, 100):
        #     listwidget.insertItem(item, "item " + str(item))

        # tool_bar_layout.addWidget(listwidget)

        tableWidget = QTableWidget()
        tableWidget.setAccessibleName("tableViewResult")
        tableWidget.setStyleSheet(
            """
                QTableWidget[accessibleName="tableViewResult"] {
                    border: none;
                    min-height: 400px;
                    min-width: 1080px;
                    max-width: 1080px;
                    max-height: 400px;
                    background-color: white;
                    color: white;
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
