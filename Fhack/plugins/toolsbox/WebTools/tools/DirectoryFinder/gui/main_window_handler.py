
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QLabel
)
from PyQt5.QtCore import Qt

from .custom_widgets.table_view_result_show import TableViewShowResult


class MainWindowHandler(QWidget):
    def __init__(self, parent=None, parent_layout=None):
        super().__init__()
        self.__init_ui__()

    @staticmethod
    def __add_controls__(org_layout):

        def add_table_view_show_urls_result():
            """ this function create table view for showing tested url and draw them for user """
            tool_bar_layout = QHBoxLayout()
            tool_bar_layout.addStretch()
            tool_bar_layout.setContentsMargins(0, 0, 0, 0)

            data_set = TableViewShowResult()

            tool_bar_layout.addWidget(data_set)
            org_layout.addLayout(tool_bar_layout)

        def add_status_table_result_labels():

            layout = QHBoxLayout()
            layout.addStretch()
            layout.setContentsMargins(0, 0, 0, 0)

            all_urls_label = QLabel("all labels: ")
            all_urls_label.setAccessibleName("labels")
            all_urls_label.setStyleSheet("""
                [accessibleName="labels"] {
                    color: white;
                    
                }
            """)
            layout.addWidget(all_urls_label)
            org_layout.addLayout(layout)

        add_status_table_result_labels()
        add_table_view_show_urls_result()

    def __init_ui__(self):
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.__add_controls__(main_layout)

        self.setLayout(main_layout)
