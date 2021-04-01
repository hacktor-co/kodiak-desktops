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
    QSizePolicy, QScrollArea
)
from PyQt5.QtCore import (
    Qt, QSize,
    QRect, QCoreApplication
)
from PyQt5.QtGui import (
    QIcon, QPixmap
)

from commons.constants.app_paths import AppPaths
from utils.media_screen import MediaScreen

from .main_window_style import DashboardMainWindowStyles


class DashboardMainWindow(QMainWindow):

    def __init__(self, gui_concentrate_handler, parent=None):
        super(DashboardMainWindow, self).__init__(parent)

        self.gui_concentrate_handler = gui_concentrate_handler

        self.__setup_ui__()

    def __setup_ui__(self):
        self.setObjectName(DashboardMainWindowStyles.main_page_style[0])
        self.setWindowModality(Qt.ApplicationModal)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAcceptDrops(False)
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.setMouseTracking(True)
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(DashboardMainWindowStyles.central_widget_style)

        # Add Central Layout
        self.central_vlayout = QVBoxLayout(self.central_widget)
        self.central_vlayout.setContentsMargins(0, 0, 0, 0)
        self.central_vlayout.setObjectName("central_vlayout")

        # Add Containers
        self.containers = QFrame(self.central_widget)
        self.containers.setObjectName(DashboardMainWindowStyles.main_window_containers_style[0])
        self.containers.setStyleSheet(DashboardMainWindowStyles.main_window_containers_style[1])
        self.containers.setFrameShape(QFrame.NoFrame)
        self.containers.setFrameShadow(QFrame.Plain)
        self.containers.setLineWidth(0)

        # Add Containers Layout
        self.containers_gridlayout = QGridLayout(self.containers)
        self.containers_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.containers_gridlayout.setSpacing(0)
        self.containers_gridlayout.setObjectName("containers_gridlayout")

        # Add Scroll Layout
        self.navigation_scroll_layout = QScrollArea(self.containers)
        self.navigation_scroll_layout.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.navigation_scroll_layout.setObjectName(DashboardMainWindowStyles.navigation_scroll_layout_style[0])
        self.navigation_scroll_layout.setStyleSheet(DashboardMainWindowStyles.navigation_scroll_layout_style[1])
        self.navigation_scroll_layout.setWidgetResizable(True)
        self.navigation_scroll_layout.setMinimumSize(QSize(71, 0))
        self.navigation_scroll_layout.setMaximumSize(QSize(71, 16777215))
        # add contents
        self.navigation_scroll_layout_contents = QWidget()
        self.navigation_scroll_layout_contents.setGeometry(QRect(0, 0, 71, self.height()))
        self.navigation_scroll_layout_contents.setObjectName("scroll_area_contents_page_containers")
        # َAdd navigation_layout
        self.navigation_grid_layout = QGridLayout(self.navigation_scroll_layout_contents)
        self.navigation_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.navigation_grid_layout.setVerticalSpacing(0)
        self.navigation_grid_layout.setObjectName("navigation_grid_layout")
        # Add Navigation
        self.navigation_menu = QFrame(self.navigation_scroll_layout_contents)
        self.navigation_menu.setObjectName(DashboardMainWindowStyles.navigation_menu_style[0])
        self.navigation_menu.setStyleSheet(DashboardMainWindowStyles.navigation_menu_style[1])
        self.navigation_menu.setMaximumSize(QSize(71, 16777215))
        self.navigation_menu.setFrameShape(QFrame.StyledPanel)
        self.navigation_menu.setFrameShadow(QFrame.Raised)
        # set Media Screen
        self.__media_screen__()
        # Add MainFrame
        self.main_frame = QFrame(self.containers)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(size_policy)
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
        is_extra_screen, extra_screen_width, extra_screen_height = MediaScreen().is_extra_large()
        if is_extra_screen:
            if extra_screen_height <= 800:
                self.li_hacktor.hide()
            else:
                self.li_hacktor.setGeometry(QRect(25, self.height() - 80, 22, 33))
        else:
            if extra_screen_height > 800:
                self.li_hacktor.setGeometry(QRect(25, self.height() - 80, 22, 33))
            else:
                if extra_screen_height <= 600:
                    self.li_hacktor.hide()
                else:
                    self.li_hacktor.setGeometry(QRect(25, self.height(), 22, 33))

        self.li_hacktor.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/hacktor_logo.svg"))
        self.li_hacktor.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.page_containers = QFrame(self.main_frame)
        self.page_containers.setFrameShape(QFrame.StyledPanel)
        self.page_containers.setFrameShadow(QFrame.Raised)
        self.page_containers.setObjectName("center_page_maker")
        self.page_containers.setMinimumSize(self.width() - 111, self.height() - 111)

        self.main_frame_gridLayout.addWidget(self.page_containers, 1, 0, 1, 4)
        self.page_containers_grid_layout = QGridLayout(self.page_containers)
        self.page_containers_grid_layout.setObjectName("page_containers_gridLayout")

        from ...components.menu_containers.menu_containers import MenuContainers
        self.menu = MenuContainers(
            self.page_containers_grid_layout, gui_concentrate_handler=self.gui_concentrate_handler
        )
        self.menu.setup_ui(
            navigation_item_vlayout=self.navigation_item_vlayout, containers=self.containers,
            page_containers=self.page_containers
        )
        from ...components.top_navigation_bar_containers.top_navigation_bar_containers import TopNavigationBarContainers
        TopNavigationBarContainers(
            gui_concentrate_handler=self.gui_concentrate_handler
        ).setup_ui(containers=self.main_frame, main_gridLayout=self.main_frame_gridLayout)

        main_icon = QIcon()
        main_icon.addPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/main_logo.ico"))
        self.setWindowIcon(main_icon)
        self.setAutoFillBackground(False)
        self.setStyleSheet(DashboardMainWindowStyles.main_page_style[1])
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.navigation_grid_layout.addWidget(self.navigation_menu, 0, 0, 1, 1)
        self.containers_gridlayout.addWidget(self.navigation_scroll_layout, 2, 2, 1, 1)
        self.navigation_scroll_layout.setWidget(self.navigation_scroll_layout_contents)

        # self.central_widget = QWidget(self)
        # self.central_widget.setStyleSheet(DashboardMainWindowStyles.central_widget_style)

        self.central_vlayout.addWidget(self.containers)
        self.containers_gridlayout.addWidget(self.main_frame, 2, 1, 1, 1)
        self.setCentralWidget(self.central_widget)
        self.__retranslateUi__()

    def __retranslateUi__(self):
        """
            this method for retranslate data in UI
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Kodiak"))
        self.lbl_time.setText("04:20")
        self.lbl_date.setText("2020/15/19")

    def __media_screen__(self):
        """
        this is private method for set a standard size window for Your monitor , Tablet or ...
        """
        is_small_screen, small_screen_width, small_screen_height = MediaScreen().is_small()
        is_medium_screen, medium_screen_width, medium_screen_height = MediaScreen().is_medium()
        is_large_screen, large_screen_width, large_screen_height = MediaScreen().is_large()
        is_extra_large_screen, extra_large_screen_width, extra_large_screen_height = MediaScreen().is_extra_large()

        if is_extra_large_screen:
            if extra_large_screen_height <= 900:

                self.setMinimumSize(QSize(extra_large_screen_width - (extra_large_screen_width / 4),
                                          extra_large_screen_height - (extra_large_screen_height / 4) + 100))
            else:

                self.setMinimumSize(QSize(extra_large_screen_width - (extra_large_screen_width / 4),
                                          extra_large_screen_height - (extra_large_screen_height / 6) + 50))
            self.navigation_menu.setMinimumSize(QSize(71, 700))
        elif is_large_screen:
            self.setMinimumSize(QSize(large_screen_width - 200, large_screen_height - 90))
            self.navigation_menu.setMinimumSize(QSize(71, 550))
        elif is_medium_screen:
            self.setMinimumSize(QSize(medium_screen_width - 100, medium_screen_height - 100))
            self.navigation_menu.setMinimumSize(QSize(71, 700))
        elif is_small_screen:
            self.setMinimumSize(QSize(small_screen_width - 150, small_screen_width - 250))
            self.navigation_menu.setMinimumSize(QSize(71, 700))
        else:
            # any thing else
            self.setMinimumSize(QSize(1150, 800))
            self.navigation_menu.setMinimumSize(QSize(71, 700))

        # Delete From Memory
        del is_small_screen, is_medium_screen, is_large_screen
        del small_screen_width, medium_screen_width, large_screen_width
        del small_screen_height, medium_screen_height, large_screen_height
