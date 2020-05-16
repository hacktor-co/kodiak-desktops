# -*- coding: utf-8 -*-
"""
    - Created on May 15/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create main window of application as dashboard

    - [mjghasempour, abolfazl]
"""

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap

from commons.constants.app_paths import AppPaths
from .main_window_style import DashboardMainWindowStyles


class DashboardMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(DashboardMainWindow, self).__init__(parent)
        self.__setup_ui__()

    def __setup_ui__(self):
        self.setObjectName(DashboardMainWindowStyles.main_page_style[0])
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(1346, 928)
        self.setMinimumSize(QSize(1346, 928))
        self.setMaximumSize(QSize(1346, 928))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAcceptDrops(False)

        main_icon = QIcon()
        main_icon.addPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/main_logo.ico"))
        self.setWindowIcon(main_icon)
        self.setAutoFillBackground(False)
        self.setStyleSheet(DashboardMainWindowStyles.main_page_style[1])
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.centralWidget = QWidget(self)
        self.centralWidget.setStyleSheet(DashboardMainWindowStyles.central_widget_style)

        # fix on line 34 of main window in kodiak test2
