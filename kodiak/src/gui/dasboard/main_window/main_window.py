# -*- coding: utf-8 -*-
"""
    - Created on May 15/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create main window of application as dashboard

    - [mjghasempour, abolfazl]
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout, QFrame,
    QLabel
)
from PyQt5.QtCore import (
    Qt, QSize,
    QRect, QCoreApplication
)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)

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
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Add Vertical Layout
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Add
        self.containers = QFrame(self.centralwidget)
        self.containers.setObjectName(DashboardMainWindowStyles.main_window_containers_style[0])
        self.containers.setStyleSheet(DashboardMainWindowStyles.main_window_containers_style[1])
        self.containers.setFrameShape(QFrame.NoFrame)
        self.containers.setFrameShadow(QFrame.Plain)
        self.containers.setLineWidth(0)

        # Add Navigation
        self.navigation_menu = QFrame(self.containers)
        self.navigation_menu.setObjectName(DashboardMainWindowStyles.navigation_menu_style[0])
        self.navigation_menu.setStyleSheet(DashboardMainWindowStyles.navigation_menu_style[1])
        self.navigation_menu.setGeometry(QRect(1275, -10, 71, 948))
        self.navigation_menu.setFrameShape(QFrame.StyledPanel)
        self.navigation_menu.setFrameShadow(QFrame.Raised)

        # Add pic_main_logo
        self.pic_main_logo = QLabel(self.navigation_menu)
        self.pic_main_logo.setGeometry(QRect(13, 40, 44, 71))
        self.pic_main_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/kodiak_icon.svg"))
        self.pic_main_logo.setObjectName("pic_main_logo")

        # Add LblTime
        self.lbl_time = QLabel(self.navigation_menu)
        self.lbl_time.setGeometry(QRect(0, 120, 69, 20))
        self.lbl_time.setObjectName(DashboardMainWindowStyles.lbl_time_style[0])
        self.lbl_time.setStyleSheet(DashboardMainWindowStyles.lbl_time_style[1])
        self.lbl_time.setAlignment(Qt.AlignCenter)

        # Add lblDate
        self.lbl_date = QLabel(self.navigation_menu)
        self.lbl_date.setGeometry(QRect(0, 140, 71, 21))
        self.lbl_date.setObjectName(DashboardMainWindowStyles.lbl_date_style[0])
        self.lbl_date.setStyleSheet(DashboardMainWindowStyles.lbl_date_style[1])
        self.lbl_date.setAlignment(Qt.AlignCenter)

        self.verticalLayoutWidget = QWidget(self.navigation_menu)
        self.verticalLayoutWidget.setGeometry(QRect(0, 290, 64, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        from ..components.menu_containers.menu_containers import MenuContainers
        MenuContainers().setup_ui(verticalLayoutWidget=self.verticalLayoutWidget, containers=self.containers)

        from ..components.top_navigation_bar_containers.top_navigation_bar_containers import TopNavigationBarContainers
        TopNavigationBarContainers().setup_ui(containers=self.containers)

        main_icon = QIcon()
        main_icon.addPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/main_logo.ico"))
        self.setWindowIcon(main_icon)
        self.setAutoFillBackground(False)
        self.setStyleSheet(DashboardMainWindowStyles.main_page_style[1])
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.centralWidget = QWidget(self)
        self.centralWidget.setStyleSheet(DashboardMainWindowStyles.central_widget_style)
        self.verticalLayout.addWidget(self.containers)
        self.setCentralWidget(self.centralwidget)

        self.__retranslateUi__()

    def __retranslateUi__(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Kodiak"))
        self.lbl_time.setText("04:20")
        self.lbl_date.setText("2020/15/19")
