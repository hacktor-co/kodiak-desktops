
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QLabel, QRadioButton, QButtonGroup, QFrame,
    QLineEdit, QFileDialog
)
from PyQt5.QtCore import Qt, pyqtSignal

from .custom_widgets.table_view_result_show import TableViewShowResult
from ..tool_api_handler import execute_tool
from .styles.main_window_handler_styles import *

from functools import partial
import threading

class MainWindowHandler(QWidget):

    def __init__(self, parent=None, parent_layout=None):
        super().__init__()
        self.__init_ui__()

    def __execute_tool__(self):
        counter = 0
        success_url = 0
        failed_url = 0
        self.data_set.clear_all_rows()

        for item in execute_tool(message_pack={
            "Rhost": self.target_input.text(),
            "ImportFilePath":
                "../test/1.txt",
            "UseLocalDatabase": False
        }):
            try:
                if item["response"]["result"]["code"] == 200:
                    success_url += 1
                    self.all_success_urls_label.setText("All success urls: " + str(success_url))
                else:
                    failed_url += 1
                    self.all_faild_urls_label.setText("All faild urls: " + str(failed_url))
            except Exception:
                pass

            self.data_set.add_result_to_display(item)
            self.all_urls_label.setText("All urls: " + str(counter))
            counter += 1

    def run_tool(self):
        thread = threading.Thread(target=self.__execute_tool__)
        thread.start()

    def __add_export_section__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(39, 0, 0, 20)

        def open_file(parent):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(
                parent, "QFileDialog.getOpenFileName()", "",
                "TXT Files (*.txt);;CSV Files (*.csv);;HTML Files (*.html);", options=options
            )
            if fileName:
                parent.path_input.setText(fileName)

        select_path_button = QPushButton()
        select_path_button.clicked.connect(partial(open_file, self))
        select_path_button.setText("select")
        select_path_button.setAccessibleName(select_path_button_style[0])
        select_path_button.setStyleSheet(select_path_button_style[1])

        layout.addWidget(select_path_button)

        self.path_input = QLineEdit()
        self.path_input.setAccessibleName(target_input_line_edit[0])
        self.path_input.setStyleSheet(target_input_line_edit[1])

        layout.addWidget(self.path_input)

        export_path_text = QLabel("Export path: ")
        export_path_text.setAccessibleName(all_labels[0])
        export_path_text.setStyleSheet(all_labels[1])
        layout.addWidget(export_path_text)

        self.main_layout.addLayout(layout)

    def __add_input_target_url__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(40, 0, 0, 20)

        start_button = QPushButton()
        start_button.setText("start")
        start_button.setAccessibleName(start_btn_style[0])
        start_button.setStyleSheet(start_btn_style[1])

        start_button.clicked.connect(self.run_tool)

        layout.addWidget(start_button)

        self.target_input = QLineEdit()
        self.target_input.setAccessibleName(target_input_line_edit[0])
        self.target_input.setStyleSheet(target_input_line_edit[1])
        layout.addWidget(self.target_input)

        target_url_text = QLabel("Target url: ")
        target_url_text.setAccessibleName(all_labels[0])
        target_url_text.setStyleSheet(all_labels[1])
        layout.addWidget(target_url_text)

        self.main_layout.addLayout(layout)

    def __add_test_kind_section__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(20, 10, 10, 100)

        file_option_frame = QFrame()
        file_option_frame.setContentsMargins(65, 50, 0, 0)
        file_option_layout = QHBoxLayout()
        file_option_layout.addStretch()
        file_option_frame.setLayout(file_option_layout)
        file_option_frame.hide()

        def open_file(parent):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(
                parent, "QFileDialog.getOpenFileName()", "",
                "All Files (*);;Python Files (*.py)", options=options
            )
            if fileName:
                parent.file_path_edit_text.setText(fileName)

        open_file_dialog_btn = QPushButton("select")
        open_file_dialog_btn.setAccessibleName(open_file_dialog_btn_style[0])
        open_file_dialog_btn.setStyleSheet(open_file_dialog_btn_style[1])
        open_file_dialog_btn.clicked.connect(partial(open_file, self))
        file_option_layout.addWidget(open_file_dialog_btn)

        self.file_path_edit_text = QLineEdit()
        self.file_path_edit_text.setAccessibleName(file_path_edit_text_style[0])
        self.file_path_edit_text.setStyleSheet(file_path_edit_text_style[1])
        file_option_layout.addWidget(self.file_path_edit_text)

        file_path_label = QLabel("File path: ")
        file_path_label.setAccessibleName(all_labels[0])
        file_path_label.setStyleSheet(all_labels[1])

        file_option_layout.addWidget(file_path_label)

        layout.addWidget(file_option_frame)

        radio_btns_vlayout = QVBoxLayout()
        radio_btns_vlayout.addStretch()
        radio_btns_vlayout.setContentsMargins(0, 0, 0, 0)

        radio_groups = QButtonGroup()

        def check_file_test_type(parent):
            if parent.radio_btn_test_from_file.isChecked():
                file_option_frame.show()

        def check_database_test_type(parent):
            if parent.radio_btn_test_from_db.isChecked():
                file_option_frame.hide()

        self.radio_btn_test_from_db = QRadioButton("Test from database")
        self.radio_btn_test_from_db.setLayoutDirection(Qt.LeftToRight)
        self.radio_btn_test_from_db.setChecked(True)
        self.radio_btn_test_from_db.setAccessibleName(all_radio_buttons[0])
        self.radio_btn_test_from_db.setStyleSheet(all_radio_buttons[1])
        self.radio_btn_test_from_db.clicked.connect(partial(check_database_test_type, self))

        self.radio_btn_test_from_file = QRadioButton("Test from file")
        self.radio_btn_test_from_file.setLayoutDirection(Qt.LeftToRight)
        self.radio_btn_test_from_file.setAccessibleName(all_radio_buttons[0])
        self.radio_btn_test_from_file.clicked.connect(partial(check_file_test_type, self))

        self.radio_btn_test_from_file.setStyleSheet(all_radio_buttons[1])

        radio_groups.addButton(self.radio_btn_test_from_db)
        radio_groups.addButton(self.radio_btn_test_from_file)

        radio_btns_vlayout.addWidget(self.radio_btn_test_from_db)
        radio_btns_vlayout.addWidget(self.radio_btn_test_from_file)

        layout.addLayout(radio_btns_vlayout)

        self.main_layout.addLayout(layout)

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

        self.all_success_urls_label = QLabel("All success urls: 0")
        self.all_success_urls_label.setAccessibleName(all_labels[0])
        self.all_success_urls_label.setStyleSheet(all_labels[1])
        self.all_success_urls_label.setContentsMargins(250, 0, 0, 0)
        layout.addWidget(self.all_success_urls_label)

        self.all_faild_urls_label = QLabel("All faild urls: 0")
        self.all_faild_urls_label.setAccessibleName(all_labels[0])
        self.all_faild_urls_label.setStyleSheet(all_labels[1])
        self.all_faild_urls_label.setContentsMargins(250, 0, 0, 0)
        layout.addWidget(self.all_faild_urls_label)

        self.all_urls_label = QLabel("All urls: 0")
        self.all_urls_label.setAccessibleName(all_labels[0])
        self.all_urls_label.setStyleSheet(all_labels[1])
        layout.addWidget(self.all_urls_label)

        self.main_layout.addLayout(layout)

    def __init_ui__(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.__add_export_section__()
        self.__add_input_target_url__()
        self.__add_test_kind_section__()
        self.__add_counter_status_section__()
        self.__add_table_view__()

        self.setLayout(self.main_layout)
