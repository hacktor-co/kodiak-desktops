"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QHBoxLayout, QWidget, QApplication,
    QAction
)

from .gui.dialogs.wdialog_db_managment_handler import DbManagmentWindow
from .gui.main_window_handler import MainWindowHandler
from .gui.styles.gui_handler_styles import *


class GUIHandler(QMainWindow):

    def init(self, parent=None):
        super(GUIHandler, self).__init__(parent=parent)
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
        # self.__add_setting_menu_bar__(menubar)
        # self.__add__help_menu_bar__(menubar)

        self.__add_widgets__()

    def __add__help_menu_bar__(self, menubar):
        help_menu = menubar.addMenu("Help")
        help_menu.setAccessibleName(menubar_styles[0])
        help_menu.setStyleSheet(menubar_styles[1])

        help_help = QAction('Help', self)
        help_update = QAction('Update', self)
        help_about = QAction('About', self)

        help_menu.addAction(help_help)
        help_menu.addAction(help_update)
        help_menu.addAction(help_about)

    def __add_setting_menu_bar__(self, menubar):
        setting_menu = menubar.addMenu("Setting")
        setting_menu.setAccessibleName(menubar_styles[0])
        setting_menu.setStyleSheet(menubar_styles[1])

        setting_manage_db = QAction('Manage db', self)

        def on_manage_db():
            DbManagmentWindow(parent=self)

        setting_manage_db.triggered.connect(on_manage_db)

        # setting_tool_config = QAction('Tool Config', self)
        #
        # setting_menu.addAction(setting_tool_config)
        setting_menu.addAction(setting_manage_db)

    def __add_widgets__(self):
        widget = QWidget(self)

        main_layout = QHBoxLayout(widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addStretch()

        mainwindow_handler = MainWindowHandler(self, parent_layout=main_layout)

        main_layout.addWidget(mainwindow_handler)

        self.setCentralWidget(widget)

    def execute_app(self):
        self.init()
        self.show()
