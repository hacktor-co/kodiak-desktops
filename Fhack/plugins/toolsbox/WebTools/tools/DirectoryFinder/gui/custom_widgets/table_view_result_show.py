
from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import Qt

from ..styles.custom_widgets_styles import table_view_show_result
from ...tool_api_handler import execute_tool


class TableViewShowResult(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setAccessibleName(table_view_show_result[0])
        self.setStyleSheet(table_view_show_result[1])

        self.setColumnCount(2)

        self.setHorizontalHeaderItem(0, QTableWidgetItem("Url"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Status"))

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.setLayoutDirection(Qt.LeftToRight)

        self.set_data()

    def set_data(self):
        for item in execute_tool(message_pack={
            "Rhost": "http://hacktor.co",
            "ImportFilePath": "/Users/topcoder/Home/Projects/Corps/HackTor/projects/FHack/test/1.txt",
            "UseLocalDatabase": False
        }):
            # print(item)
            try:
                # TODO: problem here
                if item["response"]["result"]["url"] is not None:
                    row_position = self.rowCount()
                    self.insertRow(row_position)
                    self.setItem(row_position, 0, QTableWidgetItem(item["response"]["result"]["url"]))
                    self.setItem(row_position, 1, QTableWidgetItem("hello"))
            except Exception as error:
                print(error)