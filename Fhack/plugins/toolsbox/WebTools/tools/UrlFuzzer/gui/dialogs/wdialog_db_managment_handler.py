"""
    - Created on Oct 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - dialog window for managing the database of tool package
"""

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton,
    QLabel, QRadioButton, QCheckBox,
    QLineEdit, QTableWidget, QTableWidgetItem,
    QHBoxLayout
)
from PyQt5.QtCore import Qt

from ..custom_widgets.table_view_database_manage import TableViewShowDb
from ..styles.wdialog_db_managment_handler_styles import *

class DbManagmentWindow(QDialog):

    def __init__(self, parent):
        super(DbManagmentWindow, self).__init__(parent)
        self.__init_ui__()
        self.exec()

        # AdminFinderModel.create(path="admin").save()
        # AdminFinderModel.create(path="admin").save()
        # DataBaseHelper().close()

    def __add_languages_layout__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(20, 0, 20, 20)

        self.v_main_layout.addLayout(layout)

    def __add_search_layout__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(20, 0, 20, 20)

        btn_search = QPushButton("Search")
        layout.addWidget(btn_search)

        self.v_main_layout.addLayout(layout)

    def __add_raw_query_select_layout__(self):

        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(20, 0, 20, 20)

        btn_run_query = QPushButton("RUN")
        btn_run_query.setAccessibleName(btn_run_query_style[0])
        btn_run_query.setStyleSheet(btn_run_query_style[1])
        layout.addWidget(btn_run_query)

        line_edit_get_query = QLineEdit()
        line_edit_get_query.setAccessibleName(line_edit_get_raw_query_style[0])
        line_edit_get_query.setStyleSheet(line_edit_get_raw_query_style[1])
        layout.addWidget(line_edit_get_query)

        lable = QLabel("Raw query: ")
        lable.setAccessibleName(raw_query_lable_style[0])
        lable.setStyleSheet(raw_query_lable_style[1])
        layout.addWidget(lable)

        self.v_main_layout.addLayout(layout)

    def __add_tableview_layout__(self):
        db_tableview_result = TableViewShowDb()
        self.v_main_layout.addWidget(db_tableview_result)

    def __init_ui__(self):
        self.setAccessibleName(main_qdialog_style[0])
        self.setStyleSheet(main_qdialog_style[1])
        self.v_main_layout = QVBoxLayout()
        self.v_main_layout.addStretch()
        self.v_main_layout.setContentsMargins(0, 0, 0, 0)

        self.__add_search_layout__()
        self.__add_raw_query_select_layout__()
        self.__add_tableview_layout__()

        self.setLayoutDirection(Qt.RightToLeft)
        self.setLayout(self.v_main_layout)
