"""
    - Created on May 24/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create central page controller and maker
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, 
    QDesktopWidget
)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)
from PyQt5.QtCore import (
    Qt, QSize,
    QRect, QCoreApplication
)

from .centeral_page_maker_style import CentralPageMakerStyle


class CenteralPageMaker:

    def __init__(self, containers: QFrame):
        super(CenteralPageMaker, self).__init__()
        self.__setup_ui__(containers)

    @staticmethod
    def __setup_ui__(containers: QFrame):
        page_containers = QFrame(containers)
        page_containers.setGeometry(QRect(0, 0, containers.width()+71, containers.height()+71))
        page_containers.setFrameShape(QFrame.StyledPanel)
        page_containers.setFrameShadow(QFrame.Raised)
        page_containers.setObjectName("centeral_page_maker")
        from .components.registered_part.registered import Registered
        Registered().setup_ui(containers=page_containers)
        from .components.unregistered_part.unregistered import Unregistered
        Unregistered().setup_ui(containers=page_containers)
        # lbl_registered
        lbl_registered = QLabel(page_containers)
        if QDesktopWidget().geometry().height()<800:
            lbl_registered.setGeometry(QRect((((containers.width()+900)/2)-900)+111, 0, 111, 32))
        else:
            lbl_registered.setGeometry(QRect((((containers.width()+900)/2)-900)+111, 10, 111, 32))
        
        lbl_registered.setMinimumSize(QSize(91, 32))
        lbl_registered.setObjectName(CentralPageMakerStyle.lbl_registered_style[0])
        lbl_registered.setStyleSheet(CentralPageMakerStyle.lbl_registered_style[1])
        lbl_registered.setAlignment(Qt.AlignCenter)
        # lbl_unregistered
        lbl_unregistered = QLabel(page_containers)
        if QDesktopWidget().geometry().height()<800:
            lbl_unregistered.setGeometry(QRect((((containers.width()+900)/2)-900)+111, 285, 141, 32))
        else:
            lbl_unregistered.setGeometry(QRect((((containers.width()+900)/2)-900)+111, 385, 141, 32))
        lbl_unregistered.setMinimumSize(QSize(91, 32))
        lbl_unregistered.setObjectName(CentralPageMakerStyle.lbl_unregistered_style[0])
        lbl_unregistered.setStyleSheet(CentralPageMakerStyle.lbl_unregistered_style[1])
        lbl_unregistered.setAlignment(Qt.AlignCenter)
        # lbl_title
        lbl_title = QLabel(page_containers)
        lbl_title.setGeometry(QRect(441, 10, 281, 16))
        lbl_title.setObjectName(CentralPageMakerStyle.lbl_title_style[0])
        lbl_title.setStyleSheet(CentralPageMakerStyle.lbl_title_style[1])
        
        _translate = QCoreApplication.translate
        lbl_registered.setText(_translate("Form", "REGISTERED"))
        lbl_unregistered.setText(_translate("Form", "UNREGISTERED"))
        containers.clearMask()
        page_containers.setVisible(True)