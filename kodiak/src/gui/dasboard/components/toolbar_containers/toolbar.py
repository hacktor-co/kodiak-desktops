"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QFrame,
    QLabel, QHBoxLayout,
    QGridLayout, QDesktopWidget,
    QWidget
)
from PyQt5.QtCore import (
    Qt, QRect, QPoint,
    QCoreApplication, QSize
)
from PyQt5.QtGui import (

    QIcon, QPixmap,
    QCursor
)

from utils.media_screen import MediaScreen
from .toolbar_styles import ToolBarStyles
from ....utils.utils_clicked_event import UtilsClick

from functools import partial


class ToolBar(QFrame):
    def __init__(self, main_page: QFrame, parent: QFrame):
        super(ToolBar, self).__init__()
        self.is_first: bool = False
        self.main_page: QFrame = main_page
        self.parent: QFrame = parent
        self.default_screen_width: int = self.main_page.width()
        self.default_screen_height: int = self.main_page.height()
        self.is_drag: bool = True

    def setup_ui(self, containers: QFrame):
        #  self.pressed:bool = False
        # self.toolbar_frame = QFrame(containers)
        self.setMaximumSize(QSize(16777215, 41))
        self.setLayoutDirection(Qt.RightToLeft)
        self.setObjectName(ToolBarStyles.toolbar_minimize_style[0])
        self.setStyleSheet(ToolBarStyles.toolbar_minimize_style[1])

        self.toolbar_vlayout = QVBoxLayout(self)
        self.toolbar_vlayout.setContentsMargins(0, 0, 5, 0)
        self.toolbar_vlayout.setSpacing(0)
        self.toolbar_vlayout.setObjectName("toolbar_vlayout")
        self.toolbar_components_frame = QFrame(self)
        self.toolbar_components_frame.setMinimumSize(QSize(111, 41))
        self.toolbar_components_frame.setMaximumSize(QSize(111, 41))
        self.toolbar_components_frame.setFrameShape(QFrame.StyledPanel)
        self.toolbar_components_frame.setFrameShadow(QFrame.Raised)
        self.toolbar_components_frame.setObjectName("toolbar_components_frame")
        self.toolbar_components_vlayout = QHBoxLayout(self.toolbar_components_frame)
        self.toolbar_components_vlayout.setContentsMargins(0, 0, 0, 0)
        self.toolbar_components_vlayout.setObjectName("toolbar_components_vlayout")

        self.btn_close = QLabel(self.toolbar_components_frame)
        self.btn_close.setGeometry(QRect(1310, 5, 23, 23))
        self.btn_close.setMaximumSize(23, 23)
        self.btn_close.setObjectName(ToolBarStyles.btn_close_style[0])
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        UtilsClick.clickable(self.btn_close).connect(lambda: QCoreApplication.exit())
        self.btn_close.setStyleSheet(ToolBarStyles.btn_close_style[1])
        self.toolbar_components_vlayout.addWidget(self.btn_close)

        self.btn_maximize = QLabel(self.toolbar_components_frame)
        self.btn_maximize.setGeometry(QRect(1280, 5, 23, 23))
        self.btn_maximize.setMaximumSize(23, 23)
        UtilsClick.clickable(self.btn_maximize).connect(partial(self.maximize_window))
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximize.setObjectName(ToolBarStyles.btn_maximize_style[0])
        self.btn_maximize.setStyleSheet(ToolBarStyles.btn_maximize_style[1])
        self.toolbar_components_vlayout.addWidget(self.btn_maximize)

        self.btn_minimize = QLabel(self.toolbar_components_frame)
        self.btn_minimize.setGeometry(QRect(1250, 5, 23, 23))
        self.btn_minimize.setMaximumSize(23, 23)
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        UtilsClick.clickable(self.btn_minimize).connect(self.minimized_window)
        self.btn_minimize.setObjectName(ToolBarStyles.btn_minimize_style[0])
        self.btn_minimize.setStyleSheet(ToolBarStyles.btn_minimize_style[1])
        self.toolbar_components_vlayout.addWidget(self.btn_minimize)
        self.toolbar_vlayout.addWidget(self.toolbar_components_frame)

    def maximize_window(self, x=None, y=None):
        """this method for maximize windows
        """
        self.is_first = not self.is_first
        window_width: int = int(QDesktopWidget().screenGeometry(-1).width())
        window_height: int = int(QDesktopWidget().screenGeometry(-1).height())

        if self.is_first:

            # when window from minimize to maximize
            self.parent.setGeometry(0, 0, window_width, window_height)
            self.parent.lay.setContentsMargins(0, 0, 0, 0)
            self.main_page.setStyleSheet(ToolBarStyles.main_page_maximaize_style)
            self.main_page.navigation_menu.setStyleSheet(ToolBarStyles.navigation_maximaize_menu)
            self.main_page.li_hacktor.setGeometry(QRect(25, self.main_page.height(), 22, 33))
            self.setStyleSheet(ToolBarStyles.toolbar_maximaize_style)

        else:
            # when window from minimize maximize to  minimize

            if x is None or y is None:
                """
                    window minimized go to the center on Screen
                """
                x_window: int = int((window_width - self.default_screen_width) / 2) - 50
                y_window: int = int((window_height - self.default_screen_height) / 2) - 50
                self.parent.setGeometry(x_window, y_window, self.default_screen_width, self.default_screen_height)
            else:
                """
                    window minimized go to client drag position
                """
                self.parent.setGeometry(x, y, self.default_screen_width, self.default_screen_height)

            # set setting when minimize
            self.parent.lay.setContentsMargins(50, 50, 50, 50)
            self.main_page.setStyleSheet(ToolBarStyles.main_page_minimaize_style)
            self.main_page.navigation_menu.setStyleSheet(ToolBarStyles.navigation_minimaize_menu)
            self.setStyleSheet(ToolBarStyles.toolbar_minimize_style[1])
            # hacktor-icon end of navigation menu
            is_extra_screen, extra_screen_width, extra_screen_height = MediaScreen().is_extra_large()
            if is_extra_screen:
                self.main_page.li_hacktor.setGeometry(QRect(25, self.main_page.height() - 80, 22, 33))
            else:
                if extra_screen_height > 800:
                    self.main_page.li_hacktor.setGeometry(QRect(25, self.main_page.height() - 80, 22, 33))
                else:
                    self.main_page.li_hacktor.setGeometry(QRect(25, self.main_page.height(), 22, 33))
        # hide all frame
        self.main_page.menu.hide_all_frame()
        self.parent.setCursor(Qt.ArrowCursor)

    def minimized_window(self):
        """
        this method for do minimize window
        """
        self.parent.setCursor(Qt.ArrowCursor)
        self.parent.setWindowState(Qt.WindowMinimized)

    def mousePressEvent(self, event):
        """this method for when mouse pressed
        """
        if event.buttons() == Qt.LeftButton:
            self.parent.oldPos = event.globalPos()
            # component buttons in tool bar not draggable
            if event.pos().x() <= self.main_page.width() - self.toolbar_components_frame.width():
                self.is_drag = True
            else:
                self.is_drag = False
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """this method for when mouse drag and moving
        """
        if event.buttons() == Qt.LeftButton and self.is_drag:
            self.parent.setCursor(Qt.ClosedHandCursor)
            delta = QPoint(event.globalPos() - self.parent.oldPos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.parent.oldPos = event.globalPos()

            if self.is_first:

                x_location = event.pos().x()

                if x_location >= 900:
                    self.maximize_window(x=x_location - (self.parent.width() / 2), y=event.pos().y() - 74)
                else:
                    self.maximize_window(x=(self.parent.x() + delta.x()) - 100, y=event.pos().y() - 74)

        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """this method for when mouse drop
        """
        self.parent.offset = None
        self.parent.setCursor(Qt.ArrowCursor)
        super().mouseReleaseEvent(event)
