"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QFrame,
    QLabel
)
from PyQt5.QtCore import (Qt, QRect, QCoreApplication)
from PyQt5.QtGui import (

    QIcon, QPixmap,
    QCursor
)

from commons.constants.app_paths import AppPaths
from .toolbar_styles import ToolBarStyles

from  ....utils.utils_clicked_event import UtilsClick


class ToolBar:
    def __init__(self):
        super(ToolBar, self).__init__()

    def setup_ui(self, containers: QFrame, parent):

        self.frame = QFrame(containers)
        self.frame.setGeometry(QRect(0, 0, 1341, 41))
        self.frame.setStyleSheet(ToolBarStyles.toolbar_style[1])
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName(ToolBarStyles.toolbar_style[0])
        
        self.btn_close = QLabel(self.frame)
        self.btn_close.setGeometry(QRect(1310, 5, 23, 23))
        self.btn_close.setObjectName(ToolBarStyles.btn_close_style[0])
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        UtilsClick.clickable(self.btn_close).connect(lambda : QCoreApplication.exit())
        self.btn_close.setStyleSheet(ToolBarStyles.btn_close_style[1])
        self.btn_maximize = QLabel(self.frame)
        self.btn_maximize.setGeometry(QRect(1280, 5, 23, 23))
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximize.setObjectName(ToolBarStyles.btn_maximize_style[0])
        self.btn_maximize.setStyleSheet(ToolBarStyles.btn_maximize_style[1])

        self.btn_minimize = QLabel(self.frame)
        self.btn_minimize.setGeometry(QRect(1250, 5, 23, 23))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        UtilsClick.clickable(self.btn_minimize).connect(lambda : parent.setWindowState(Qt.WindowMinimized))
        
        self.btn_minimize.setObjectName(ToolBarStyles.btn_minimize_style[0])
        self.btn_minimize.setStyleSheet(ToolBarStyles.btn_minimize_style[1])
        
