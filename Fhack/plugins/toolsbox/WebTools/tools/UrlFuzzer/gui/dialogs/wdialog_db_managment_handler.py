
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton,
    QLabel, QRadioButton, QCheckBox,
    QLineEdit, QTableWidget, QTableWidgetItem
)

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
    def __init_ui__(self):
        self.setAccessibleName(main_qdialog_style[0])
        self.setStyleSheet(main_qdialog_style[1])

        v_main_layout = QVBoxLayout()
        v_main_layout.addStretch()
        v_main_layout.setContentsMargins(0, 0, 0, 0)

        db_tableview_result = TableViewShowDb()
        v_main_layout.addWidget(db_tableview_result)

        self.setLayout(v_main_layout)
