"""
    - Created on May 15/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create main window of application as dashboard

    - [mjghasempour, abolfazl]
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout, QFrame,
    QLabel, QGridLayout,
    QSizePolicy, QDesktopWidget
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
        if QDesktopWidget().geometry().height()<800:
            self.setMinimumSize(QSize(1150, 675))
        else:
            self.setMinimumSize(QSize(1150, 800))

        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAcceptDrops(False)
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)

        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet(DashboardMainWindowStyles.centeral_widget_style)

        # Add Central Layout
        self.central_vlayout = QVBoxLayout(self.centralwidget)
        self.central_vlayout.setContentsMargins(0, 0, 0, 0)
        self.central_vlayout.setObjectName("central_vlayout")

        # Add Containers
        self.containers = QFrame(self.centralwidget)
        self.containers.setObjectName(DashboardMainWindowStyles.main_window_containers_style[0])
        self.containers.setStyleSheet(DashboardMainWindowStyles.main_window_containers_style[1])
        self.containers.setFrameShape(QFrame.NoFrame)
        self.containers.setFrameShadow(QFrame.Plain)
        self.containers.setLineWidth(0)

        #Add Containers Layout
        self.containers_gridlayout = QGridLayout(self.containers)
        self.containers_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.containers_gridlayout.setSpacing(0)
        self.containers_gridlayout.setObjectName("containers_gridlayout")

        # Add Navigation
        self.navigation_menu = QFrame(self.containers)
        self.navigation_menu.setObjectName(DashboardMainWindowStyles.navigation_menu_style[0])
        self.navigation_menu.setStyleSheet(DashboardMainWindowStyles.navigation_menu_style[1])
        if QDesktopWidget().geometry().height()<800:
            self.navigation_menu.setMinimumSize(QSize(71, 550))
        else:
            self.navigation_menu.setMinimumSize(QSize(71, 700))
       
        self.navigation_menu.setMaximumSize(QSize(71, 16777215))
        self.navigation_menu.setFrameShape(QFrame.StyledPanel)
        self.navigation_menu.setFrameShadow(QFrame.Raised)

        #َAdd navigation_layout
        self.navigation_grid_layout = QGridLayout()
        self.navigation_grid_layout.setContentsMargins(-1, 0, 0, -1)
        self.navigation_grid_layout.setVerticalSpacing(0)
        self.navigation_grid_layout.setObjectName("navigation_grid_layout")
        self.navigation_grid_layout.addWidget(self.navigation_menu, 0, 0, 1, 1)
        self.containers_gridlayout.addLayout(self.navigation_grid_layout, 2, 2, 1, 1)

        #Add MainFrame
        self.main_frame = QFrame(self.containers)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setObjectName("main_frame")

        # Add MainFrameLayout
        self.main_frame_gridLayout = QGridLayout(self.main_frame)
        self.main_frame_gridLayout.setContentsMargins(8, 8, 8, 8)
        self.main_frame_gridLayout.setSpacing(0)
        self.main_frame_gridLayout.setObjectName("gridLayout")
        # Add pic_main_logo
        self.pic_main_logo = QLabel(self.navigation_menu)
        self.pic_main_logo.setGeometry(QRect(0, 35, 71, 71))
        self.pic_main_logo.setAlignment(Qt.AlignCenter)
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

        self.navigation_item_vlayout = QWidget(self.navigation_menu)
        self.navigation_item_vlayout.setGeometry(QRect(0, 220, 64, 431))
        self.navigation_item_vlayout.setObjectName("navigation_item_vlayout")

        # set li_hacktor_logo
        self.li_hacktor = QLabel(self.navigation_menu)
        self.li_hacktor.setAccessibleName("hacktor_logo")
        if QDesktopWidget().geometry().height()<800:
            self.li_hacktor.setGeometry(QRect(25, self.height(), 22, 33))
        else:
            self.li_hacktor.setGeometry(QRect(25, self.height()-82, 22, 33))
        self.li_hacktor.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/hacktor_logo.svg"))
        self.li_hacktor.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        
        self.page_containers = QFrame(self.main_frame)
        self.page_containers.setFrameShape(QFrame.StyledPanel)
        self.page_containers.setFrameShadow(QFrame.Raised)
        self.page_containers.setObjectName("center_page_maker")
        self.page_containers.setMinimumSize(self.width()-111,self.height()-111)
        self.main_frame_gridLayout.addWidget(self.page_containers, 1, 0, 1, 4, Qt.AlignHCenter|Qt.AlignVCenter)
        
        
        from ...components.menu_containers.menu_containers import MenuContainers
        self.menu = MenuContainers()
        self.menu.setup_ui(
            navigation_item_vlayout=self.navigation_item_vlayout, containers=self.containers,
            contaners_item=self.page_containers
        )
        
        from ...components.top_navigation_bar_containers.top_navigation_bar_containers import TopNavigationBarContainers
        TopNavigationBarContainers().setup_ui(containers=self.main_frame, main_gridLayout = self.main_frame_gridLayout)

        main_icon = QIcon()
        main_icon.addPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/main_logo.ico"))
        self.setWindowIcon(main_icon)
        self.setAutoFillBackground(False)
        self.setStyleSheet(DashboardMainWindowStyles.main_page_style[1])
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)

        # self.central_widget = QWidget(self)
        # self.central_widget.setStyleSheet(DashboardMainWindowStyles.central_widget_style)

        self.central_vlayout.addWidget(self.containers)
        self.containers_gridlayout.addWidget(self.main_frame, 2, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.__retranslateUi__()

    def __retranslateUi__(self):
        """
            this method for retranslate data in UI
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Kodiak"))
        self.lbl_time.setText("04:20")
        self.lbl_date.setText("2020/15/19")