# -*- coding: utf-8 -*-

"""
    - Created on May 15/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create main window of application as dashboard

    - [mjghasempour, abolfazl]
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap

from commons.constants.app_paths import AppPaths


class DasboardMainWindow(object):

    def setup_ui(self, main_window: QMainWindow):

        main_window.setObjectName("MainWindow")
        main_window.setWindowModality(Qt.ApplicationModal)
        main_window.resize(1346, 928)
        main_window.setMinimumSize(QSize(1346, 928))
        main_window.setMaximumSize(QSize(1346, 928))
        main_window.setContextMenuPolicy(Qt.NoContextMenu)
        main_window.setAcceptDrops(False)

        main_icon = QIcon()
        main_icon.addPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/main_logo.ico"))
