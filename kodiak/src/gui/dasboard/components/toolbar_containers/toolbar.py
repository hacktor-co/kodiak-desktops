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

from commons.constants.app_paths import AppPaths
from .toolbar_styles import ToolBarStyles
from  ....utils.utils_clicked_event import UtilsClick

from functools import partial


class ToolBar(QFrame):
    def __init__(self, main_page: QFrame ,parent: QFrame):
        super(ToolBar, self).__init__()
        self.main_page: QFrame = main_page
        self.parent: QFrame = parent
    def setup_ui(self , containers: QFrame):
        self.is_first:bool = False
      #  self.pressed:bool = False
        #self.toolbar_frame = QFrame(containers)
        self.setMinimumSize(QSize(0, 0))
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
        self.btn_close.setMaximumSize(23,23)
        self.btn_close.setObjectName(ToolBarStyles.btn_close_style[0])
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        UtilsClick.clickable(self.btn_close).connect(lambda : QCoreApplication.exit())
        self.btn_close.setStyleSheet(ToolBarStyles.btn_close_style[1])
        self.toolbar_components_vlayout.addWidget(self.btn_close)

        self.btn_maximize = QLabel(self.toolbar_components_frame)
        self.btn_maximize.setGeometry(QRect(1280, 5, 23, 23))
        self.btn_maximize.setMaximumSize(23,23)
        UtilsClick.clickable(self.btn_maximize).connect(partial(self.maximize_window))
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximize.setObjectName(ToolBarStyles.btn_maximize_style[0])
        self.btn_maximize.setStyleSheet(ToolBarStyles.btn_maximize_style[1])
        self.toolbar_components_vlayout.addWidget(self.btn_maximize)

        self.btn_minimize = QLabel(self.toolbar_components_frame)
        self.btn_minimize.setGeometry(QRect(1250, 5, 23, 23))
        self.btn_minimize.setMaximumSize(23,23)
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        UtilsClick.clickable(self.btn_minimize).connect(lambda : self.parent.setWindowState(Qt.WindowMinimized))
        self.btn_minimize.setObjectName(ToolBarStyles.btn_minimize_style[0])
        self.btn_minimize.setStyleSheet(ToolBarStyles.btn_minimize_style[1])
        self.toolbar_components_vlayout.addWidget(self.btn_minimize)
        self.toolbar_vlayout.addWidget(self.toolbar_components_frame)
        

    def maximize_window(self, x = None , y = None):
        """this method for maximize windows
        """
        self.is_first = not self.is_first
        window_width: int = int(QDesktopWidget().screenGeometry(-1).width())
        window_height: init = int(QDesktopWidget().screenGeometry(-1).height())
    
        if (self.is_first):
            #when window from minimize to maximize
            self.parent.setGeometry(0, 0, window_width, window_height)
            self.parent.lay.setContentsMargins(0,0,0,0)
            self.main_page.setStyleSheet(ToolBarStyles.main_page_maximaize_style)
            self.main_page.navigation_menu.setStyleSheet(ToolBarStyles.navigation_maximaize_menu)
            self.main_page.li_hacktor.setGeometry(QRect(25, self.main_page.height(), 22, 33))
            self.setStyleSheet(ToolBarStyles.toolbar_maximaize_style)
            
        else:
            #when window from minimize maximize to  minimize

            if x == None or y == None :
                self.parent.setGeometry((window_width-1150)/2, (window_height-800)/2, 1150, 800)
            else:
                self.parent.setGeometry(x, y, 1150, 800)

            self.parent.lay.setContentsMargins(50, 50, 50, 50)
            self.main_page.setStyleSheet(ToolBarStyles.main_page_minimaize_style)
            self.main_page.navigation_menu.setStyleSheet(ToolBarStyles.navigation_minimaize_menu)
            self.setStyleSheet(ToolBarStyles.toolbar_minimize_style[1])
            self.main_page.li_hacktor.setGeometry(QRect(25, self.main_page.height()-82, 22, 33))
        self.main_page.menu.hide_all_frame()

    def mousePressEvent(self, event):
        """this method for when mouse pressed
        """
        if event.buttons() == Qt.LeftButton:
            self.parent.oldPos = event.globalPos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """this method for when mouse drag and moveing
        """
        if event.buttons() == Qt.LeftButton:
            delta = QPoint (event.globalPos() - self.parent.oldPos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.parent.oldPos = event.globalPos()
            if  (self.is_first):
                x_location=event.pos().x()
        
                if x_location >=900:
                    self.maximize_window(x= x_location-(self.parent.width()/2), y=  event.pos().y()-74)
                else:
                    self.maximize_window(x= (self.parent.x() + delta.x())-100, y=  event.pos().y()-74)
                
        else:
            super().mouseMoveEvent(event)
            
    def mouseReleaseEvent(self, event):
        """this method for when mouse drop
        """
        self.parent.offset = None
        super().mouseReleaseEvent(event)
