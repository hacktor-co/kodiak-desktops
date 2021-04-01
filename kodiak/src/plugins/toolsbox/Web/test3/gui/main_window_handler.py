
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QLabel, QRadioButton, QButtonGroup, QFrame,
    QLineEdit, QFileDialog
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon

from .custom_widgets.table_view_result_show import TableViewShowResult
from ..tool_api_handler import execute_tool
from .styles.main_window_handler_styles import *
from ..modules.utils import get_os_info

from functools import partial
import threading


class MainWindowHandler(QWidget):

    export_path = str()
    use_tool_database = True

    def __init__(self, parent=None, parent_layout=None):
        super().__init__()
        self.__init_ui__()

    def save_result_to_file(self, input_item: str):
        try:
            print(self.export_path)
            with open(self.export_path, "w") as file:
                file.write(input_item + "\n")
                file.flush()
        except Exception as error:
            print(error)

    def __execute_tool__(self):
        counter = 0
        success_url = 0
        failed_url = 0
        self.data_set.clear_all_rows()

        for item in execute_tool(message_pack={
            "Rhost": self.target_input.text(),
            "ImportFilePath": self.myfile_path.text(),
            "UseLocalDatabase": self.use_tool_database
        }):
            try:
                if item["response"]["result"]["code"] == 200:
                    success_url += 1
                    self.all_success_urls_label.setText("All success urls: " + str(success_url))
                    self.save_result_to_file(item["response"]["result"]["url"])
                else:
                    failed_url += 1
                    self.all_faild_urls_label.setText("All faild urls: " + str(failed_url))
            except Exception:
                pass
            self.data_set.add_result_to_display(item)
            self.all_urls_label.setText("All urls: " + str(counter))
            counter += 1

    def run_tool(self):
        self.export_path = self.path_export.text()
        thread = threading.Thread(target=self.__execute_tool__)
        thread.start()

    def __add_input_target_url__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(40, 0, 0, 20)

        self.target_input = QLineEdit()
        self.target_input.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.target_input.setAccessibleName(target_input_line_edit[0])
        self.target_input.setStyleSheet(target_input_line_edit[1])
        self.target_input.setPlaceholderText("Target url")
        layout.addWidget(self.target_input)

        icon_label = QLabel()
        image = QPixmap('./plugins/toolsbox/WebTools/tools/UrlFuzzer/assets/www_icon.svg')
        image.scaled(10, 10)
        icon_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        icon_label.setPixmap(image)
        layout.addWidget(icon_label)

        self.main_layout.addLayout(layout)

    def __add_icons_section__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(240, 0, 0, 0)

        db_label = QLabel()
        image = QPixmap('./plugins/toolsbox/WebTools/tools/UrlFuzzer/assets/database.svg')
        db_label.setContentsMargins(100, 0, 0, 0)
        image.scaled(10, 10)

        db_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        db_label.setPixmap(image)

        layout.addWidget(db_label)

        file_label = QLabel()
        image = QPixmap('./plugins/toolsbox/WebTools/tools/UrlFuzzer/assets/folder.svg')

        image.scaled(10, 10)

        file_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        file_label.setPixmap(image)

        layout.addWidget(file_label)

        self.main_layout.addLayout(layout)

    def __add_test_kind_section__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(200, 0, 0, 00)

        radio_btns_vlayout = QHBoxLayout()
        radio_btns_vlayout.addStretch()
        radio_btns_vlayout.setContentsMargins(0, 5, 0, 0)

        radio_groups = QButtonGroup()

        def check_file_test_type(parent):
            if parent.radio_btn_test_from_file.isChecked():
                parent.h_myfile_select_frame.setEnabled(True)
                parent.use_tool_database = False

        def check_database_test_type(parent):
            if parent.radio_btn_test_from_db.isChecked():
                parent.h_myfile_select_frame.setEnabled(False)
                parent.use_tool_database = True

        self.radio_btn_test_from_db = QRadioButton("Use tool database")
        self.radio_btn_test_from_db.setLayoutDirection(Qt.LeftToRight)
        self.radio_btn_test_from_db.setChecked(True)
        self.radio_btn_test_from_db.setAccessibleName(all_radio_buttons[0])
        self.radio_btn_test_from_db.setStyleSheet(all_radio_buttons[1])
        self.radio_btn_test_from_db.clicked.connect(partial(check_database_test_type, self))

        self.radio_btn_test_from_file = QRadioButton("Use my file")
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

    def __add_all_urls_section__(self):

        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)

        frame = QFrame()
        v_label_layout = QVBoxLayout()

        if get_os_info()["os"] == "Windows":
            v_label_layout.setContentsMargins(776, 0, 0, 0)
        else:
            v_label_layout.setContentsMargins(827, 0, 0, 0)

        v_label_layout.addStretch()
        self.all_urls_label = QLabel("All urls: 0")
        self.all_urls_label.setAccessibleName(all_urls_label[0])
        self.all_urls_label.setStyleSheet(all_urls_label[1])

        v_label_layout.addWidget(self.all_urls_label)
        frame.setLayout(v_label_layout)
        layout.addWidget(frame)

        self.main_layout.addLayout(layout)

    def __add_table_view__(self):
        self.data_set = TableViewShowResult()

        tool_bar_layout = QHBoxLayout()
        tool_bar_layout.addStretch()
        tool_bar_layout.setContentsMargins(0, 0, 0, 0)
        tool_bar_layout.addWidget(self.data_set)

        self.main_layout.addLayout(tool_bar_layout)

    def __add_myfile_selector_section__(self):
        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)

        frame = QFrame()
        v_label_layout = QVBoxLayout()

        if get_os_info()["os"] == "Windows":
            v_label_layout.setContentsMargins(260, 0, 0, 0)
        else:
            v_label_layout.setContentsMargins(339, 0, 0, 0)

        v_label_layout.addStretch()
        self.all_faild_urls_label = QLabel("Failed url: 0")
        self.all_faild_urls_label.setAccessibleName(all_failed_urls_label_style[0])
        self.all_faild_urls_label.setStyleSheet(all_failed_urls_label_style[1])
        v_label_layout.addWidget(self.all_faild_urls_label)
        frame.setLayout(v_label_layout)
        layout.addWidget(frame)

        def open_file(parent):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getOpenFileName(
                parent, "QFileDialog.getOpenFileName()", "",
                "All text files (*.txt)", options=options
            )

            if file_name:
                parent.myfile_path.setText(file_name)

        hlayout_control = QHBoxLayout()
        hlayout_control.setContentsMargins(0, 0, 0, 0)
        hlayout_control.addStretch()
        self.h_myfile_select_frame = QFrame()
        self.h_myfile_select_frame.setDisabled(True)

        select_path_button = QPushButton()
        select_path_button.clicked.connect(partial(open_file, self))
        select_path_button.setText("Select")
        select_path_button.setAccessibleName(select_path_button_style[0])
        select_path_button.setStyleSheet(select_path_button_style[1])

        hlayout_control.addWidget(select_path_button)

        self.myfile_path = QLineEdit()
        self.myfile_path.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.myfile_path.setContentsMargins(47, 0, 20, 0)
        self.myfile_path.setPlaceholderText("File path")
        self.myfile_path.setAccessibleName(myfile_input_line_edit[0])
        self.myfile_path.setStyleSheet(myfile_input_line_edit[1])

        hlayout_control.addWidget(self.myfile_path)
        self.h_myfile_select_frame.setLayout(hlayout_control)
        layout.addWidget(self.h_myfile_select_frame)

        self.main_layout.addLayout(layout)

    def __add_counter_status_section__(self):

        layout = QHBoxLayout()
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)

        frame = QFrame()
        v_label_layout = QVBoxLayout()
        if get_os_info()["os"] == "Windows":
            v_label_layout.setContentsMargins(150, 0, 0, 10)
        else:
            v_label_layout.setContentsMargins(210, 0, 0, 10)

        v_label_layout.addStretch()
        self.all_success_urls_label = QLabel("Success urls: 0")
        self.all_success_urls_label.setAccessibleName(all_urls_label_style[0])
        self.all_success_urls_label.setStyleSheet(all_urls_label_style[1])
        v_label_layout.addWidget(self.all_success_urls_label)
        frame.setLayout(v_label_layout)
        layout.addWidget(frame)

        start_btn = QPushButton()
        start_btn.setText("Start")
        start_btn.setContentsMargins(20, 0, 0, 0)
        start_btn.setAccessibleName(start_button_style[0])
        start_btn.setStyleSheet(start_button_style[1])
        start_btn.clicked.connect(self.run_tool)

        layout.addWidget(start_btn)

        def open_file(parent):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getOpenFileName(
                parent, "QFileDialog.getOpenFileName()", "",
                "All text files (*.txt)", options=options
            )
            if file_name:
                parent.path_export.setText(file_name)

        select_path_button = QPushButton()
        select_path_button.clicked.connect(partial(open_file, self))
        select_path_button.setText("Select")
        select_path_button.setAccessibleName(select_path_button_style[0])
        select_path_button.setStyleSheet(select_path_button_style[1])

        layout.addWidget(select_path_button)

        self.path_export = QLineEdit()
        self.path_export.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.path_export.setContentsMargins(47, 0, 20, 0)
        self.path_export.setPlaceholderText("Export path")
        self.path_export.setAccessibleName(target_input_line_edit[0])
        self.path_export.setStyleSheet(target_input_line_edit[1])

        layout.addWidget(self.path_export)

        self.main_layout.addLayout(layout)

    def __init_ui__(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.__add_input_target_url__()
        self.__add_icons_section__()
        self.__add_test_kind_section__()
        self.__add_all_urls_section__()
        self.__add_myfile_selector_section__()
        self.__add_counter_status_section__()
        self.__add_table_view__()

        self.setLayout(self.main_layout)
