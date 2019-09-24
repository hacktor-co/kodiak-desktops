#!usr/bin/python3.7
"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QHBoxLayout, QWidget, QApplication,
    QAction, QMenu
)

from .gui.main_window_handler import MainWindowHandler
from .gui.styles.gui_handler_styles import *
from .tool_api.modules.database_handler import DataBaseHelper
from .tool_api.models.admin_finder_model import AdminFinderModel
from .gui.db_managment_window_handler import MainWindow as DbManagmentWindow


class MainWindow(QMainWindow):

    @staticmethod
    def init_db():
        DataBaseHelper().connect()
        DataBaseHelper().db_main.create_tables([AdminFinderModel])
        DataBaseHelper().close()

    def init(self, parent):
        super().__init__()
        self.setAccessibleName("QMainWindowStyle")
        self.setWindowTitle("Directory Finder")
        self.setStyleSheet(main_window_style)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setContentsMargins(0, 0, 0, 0)

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            # 1080 -> width of window
            # 800  -> height og window
            int((screen_size.width() - 1000) / 2),
            int((screen_size.height() - 800) / 2),
            0, 0
        )  # set the main window to center of screen

        menubar = self.menuBar()
        menubar.setLayoutDirection(Qt.LeftToRight)
        menubar.setAccessibleName(menubar_styles[0])
        menubar.setStyleSheet(menubar_styles[1])

        setting_menu = menubar.addMenu("Setting")
        setting_menu.setAccessibleName(menubar_styles[0])
        setting_menu.setStyleSheet(menubar_styles[1])

        setting_update = QAction('update', self)

        def send_update_db():
            print("update")

        setting_update.triggered.connect(send_update_db)

        setting_manage_db = QAction('manage db', self)

        def on_manage_db():
            DbManagmentWindow(parent=parent)

        setting_manage_db.triggered.connect(on_manage_db)

        setting_menu.addAction(setting_update)
        setting_menu.addAction(setting_manage_db)

        self.__add_widgets__()

    def __add_widgets__(self):
        widget = QWidget(self)

        main_layout = QHBoxLayout(widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addStretch()

        mainwindow_handler = MainWindowHandler(self, parent_layout=main_layout)

        main_layout.addWidget(mainwindow_handler)

        self.setCentralWidget(widget)

    def execute_app(self, parent=None):
        self.init(parent)
        self.init_db()
        self.show()
