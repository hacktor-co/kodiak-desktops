"""
    - Created on Oct 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - dialog window for managing the database of tool package
"""

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton,
    QLabel, QRadioButton, QCheckBox,
    QLineEdit, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QButtonGroup, QFrame
)
from PyQt5.QtCore import Qt

from ..custom_widgets.table_view_database_manage import TableViewShowDb
from ..styles.wdialog_db_managment_handler_styles import *


class DbManagmentWindow(QDialog):

    def __init__(self, parent):
        super(DbManagmentWindow, self).__init__(parent)
        self.__init_ui__()
        self.exec()

    def __add_inclued_paths_layout__(self):
        frame = QFrame()
        frame.setAccessibleName(inclued_paths_section_style[0])
        frame.setStyleSheet(inclued_paths_section_style[1])
        frame.setContentsMargins(10, 0, 10, 45)

        layout = QHBoxLayout()
        layout.addStretch()

        frame.setLayout(layout)

        radio_group = QButtonGroup()

        radio_button_login_finder = QRadioButton()
        radio_button_login_finder.setText("Login finder")
        radio_button_login_finder.setAccessibleName(radio_buttons_style[0])
        radio_button_login_finder.setStyleSheet(radio_buttons_style[1])
        radio_button_login_finder.setChecked(True)

        radio_group.addButton(radio_button_login_finder)

        layout.addWidget(radio_button_login_finder)

        label = QLabel("Paths")
        label.setAccessibleName(db_label_style[0])
        label.setStyleSheet(db_label_style[1])
        label.setContentsMargins(0, 0, 0, 40)
        layout.addWidget(label)

        self.v_main_layout.addWidget(frame)

    def __add_languages_layout__(self):
        frame = QFrame()
        frame.setAccessibleName(inclued_paths_section_style[0])
        frame.setStyleSheet(inclued_paths_section_style[1])
        frame.setContentsMargins(10, 0, 10, 45)

        layout = QHBoxLayout()
        layout.addStretch()

        button_groups = QButtonGroup()

        radio_button_php = QRadioButton()
        radio_button_php.setText("PHP")
        radio_button_php.setChecked(True)
        radio_button_php.setAccessibleName(radio_buttons_style[0])
        radio_button_php.setStyleSheet(radio_buttons_style[1])

        button_groups.addButton(radio_button_php)

        layout.addWidget(radio_button_php)

        label = QLabel("Languages")
        label.setAccessibleName(db_label_style[0])
        label.setStyleSheet(db_label_style[1])
        label.setContentsMargins(0, 0, 0, 40)
        layout.addWidget(label)

        frame.setLayout(layout)

        self.v_main_layout.addWidget(frame)

    def __add_crud_layout__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(20, 20, 20, 20)

        btn_search = QPushButton("Submit")
        layout.addWidget(btn_search)

        # btn_search = QPushButton("Insert data with file")
        # layout.addWidget(btn_search)

        self.v_main_layout.addLayout(layout)

    # def __add_raw_query_select_layout__(self):
    #
    #     layout = QHBoxLayout()
    #     layout.addStretch()
    #     layout.setContentsMargins(20, 0, 20, 20)
    #
    #     btn_run_query = QPushButton("Run")
    #     btn_run_query.setAccessibleName(btn_run_query_style[0])
    #     btn_run_query.setStyleSheet(btn_run_query_style[1])
    #     layout.addWidget(btn_run_query)
    #
    #     line_edit_get_query = QLineEdit()
    #     line_edit_get_query.setAccessibleName(line_edit_get_raw_query_style[0])
    #     line_edit_get_query.setStyleSheet(line_edit_get_raw_query_style[1])
    #     layout.addWidget(line_edit_get_query)
    #
    #     lable = QLabel("Raw query: ")
    #     lable.setAccessibleName(raw_query_lable_style[0])
    #     lable.setStyleSheet(raw_query_lable_style[1])
    #     layout.addWidget(lable)
    #
    #     self.v_main_layout.addLayout(layout)

    def __add_tableview_layout__(self):
        db_tableview_result = TableViewShowDb()
        self.v_main_layout.addWidget(db_tableview_result)

    def __init_ui__(self):
        self.setAccessibleName(main_qdialog_style[0])
        self.setStyleSheet(main_qdialog_style[1])
        self.v_main_layout = QVBoxLayout()
        self.v_main_layout.addStretch()
        self.v_main_layout.setContentsMargins(0, 0, 0, 0)

        # db_label = QLabel("Sqlite3")
        # db_label.setAccessibleName(db_label_style[0])
        # db_label.setStyleSheet(db_label_style[1])
        # db_label.setContentsMargins(20, 0, 20, 10)
        # self.v_main_layout.addWidget(db_label)

        self.__add_inclued_paths_layout__()
        self.__add_languages_layout__()
        self.__add_crud_layout__()
        # self.__add_raw_query_select_layout__()
        self.__add_tableview_layout__()

        self.setLayoutDirection(Qt.RightToLeft)
        self.setLayout(self.v_main_layout)
