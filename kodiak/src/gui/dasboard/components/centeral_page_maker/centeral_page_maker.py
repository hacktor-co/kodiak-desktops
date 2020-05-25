"""
    - Created on May 24/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create central page controller and maker
"""

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect


class CenteralPageMaker:
    
    def __init__(self, containers: QFrame):
        super(CenteralPageMaker, self).__init__()
        self.__setup_ui__(containers)

    @staticmethod
    def __setup_ui__(containers: QFrame):
        page_containers = QFrame(containers)
        page_containers.setGeometry(QRect(50, 30, 1264, 750))
        page_containers.setFrameShape(QFrame.StyledPanel)
        page_containers.setFrameShadow(QFrame.Raised)
        page_containers.setObjectName("centeral_page_maker")
