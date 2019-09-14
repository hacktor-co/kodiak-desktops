
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QLabel
)
from PyQt5.QtCore import Qt, pyqtSignal

from .custom_widgets.table_view_result_show import TableViewShowResult
from ..tool_api_handler import execute_tool


class MainWindowHandler(QWidget):

    def __init__(self, parent=None, parent_layout=None):
        super().__init__()
        self.__init_ui__()

    def __add_table_view__(self):
        self.data_set = TableViewShowResult()

        tool_bar_layout = QHBoxLayout()
        tool_bar_layout.addStretch()
        tool_bar_layout.setContentsMargins(0, 0, 0, 0)
        tool_bar_layout.addWidget(self.data_set)

        self.main_layout.addLayout(tool_bar_layout)

    def __add_counter_status_section__(self):

        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(20, 10, 10, 10)

        all_faild_urls_label = QLabel("All success urls: ")
        all_faild_urls_label.setAccessibleName("all_success_urls_labels")
        all_faild_urls_label.setStyleSheet("""
            [accessibleName="all_success_urls_labels"] {
                color: white;
                font-size: 15px;
            }
        """)
        all_faild_urls_label.setContentsMargins(250, 0, 0, 0)
        layout.addWidget(all_faild_urls_label)

        all_faild_urls_label = QLabel("All faild urls: ")
        all_faild_urls_label.setAccessibleName("all_faild_urls_labels")
        all_faild_urls_label.setStyleSheet("""
            [accessibleName="all_faild_urls_labels"] {
                color: white;
                font-size: 15px;
            }
        """)
        all_faild_urls_label.setContentsMargins(250, 0, 0, 0)
        layout.addWidget(all_faild_urls_label)

        all_urls_label = QLabel("All urls: ")
        all_urls_label.setAccessibleName("all_urls_labels")
        all_urls_label.setStyleSheet("""
            [accessibleName="all_urls_labels"] {
                color: white;
                font-size: 15px;
            }
        """)
        layout.addWidget(all_urls_label)

        self.main_layout.addLayout(layout)

        # button = QPushButton("Button")
        # button.clicked.connect(self.data_set.set_data)
        # layout.addWidget(button)

    def __init_ui__(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.__add_counter_status_section__()
        self.__add_table_view__()

        self.setLayout(self.main_layout)
