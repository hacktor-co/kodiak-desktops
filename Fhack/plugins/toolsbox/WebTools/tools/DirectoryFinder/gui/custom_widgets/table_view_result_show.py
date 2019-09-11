
from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import Qt

from ..styles.custom_widgets_styles import table_view_show_result


class TableViewShowResult(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data

        self.setAccessibleName(table_view_show_result[0])
        self.setStyleSheet(table_view_show_result[1])
        self.setContentsMargins(0, 0, 0, 0)

        self.set_data()
        self.setColumnCount(2)

        self.setHorizontalHeaderItem(0, QTableWidgetItem("Url"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Status"))
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.setLayoutDirection(Qt.LeftToRight)

    def set_data(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                newitem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
