"""
    - Created on May 24/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create central page controller and maker
"""

from PyQt5.QtWidgets import (
    QLabel, QFrame, QFormLayout, QGridLayout, QScrollArea,
    QVBoxLayout
)
from PyQt5.QtCore import (
    Qt, QSize, QRect, QCoreApplication
)

from .central_page_maker_style import CentralPageMakerStyle


class CentralPageMaker:

    def __init__(self, containers: QFrame, page_containers_grid_layout: QGridLayout, page_name: str):
        super(CentralPageMaker, self).__init__()

        self.page_name: str = page_name

        self.__setup_ui__(containers, page_containers_grid_layout)

    def __setup_ui__(self, containers: QFrame, page_containers_grid_layout: QGridLayout):
        page_containers = QFrame(containers)
        page_containers.setFrameShape(QFrame.StyledPanel)
        page_containers.setFrameShadow(QFrame.Raised)
        page_containers.setObjectName("central_page_maker")
        vl_page_containers = QVBoxLayout(page_containers)
        vl_page_containers.setObjectName("vl_page_containers")

        scroll_area_page_containers = QScrollArea(page_containers)
        scroll_area_page_containers.setObjectName(CentralPageMakerStyle.scroll_area_page_containers_style[0])
        scroll_area_page_containers.setStyleSheet(CentralPageMakerStyle.scroll_area_page_containers_style[1])
        scroll_area_page_containers.setWidgetResizable(True)
        scroll_area_page_containers.setLayoutDirection(Qt.RightToLeft)
        scroll_area_contents_page_containers = QFrame()
        scroll_area_contents_page_containers.setObjectName("scroll_area_contents_page_containers")
        scroll_area_contents_page_containers.setContentsMargins(45, 45, 45, 45)

        form_base_layout = QFormLayout(scroll_area_contents_page_containers)
        form_base_layout.setContentsMargins(0, 0, 0, 0)
        form_base_layout.setHorizontalSpacing(0)
        form_base_layout.setVerticalSpacing(100)
        form_base_layout.setObjectName("form_base_layout")

        from .components.registered_part.registered import Registered
        Registered(form_base_layout).setup_ui(containers=scroll_area_contents_page_containers)
        from .components.unregistered_part.unregistered import Unregistered
        Unregistered(form_base_layout).setup_ui(containers=scroll_area_contents_page_containers)

        # lbl_title
        lbl_title = QLabel(scroll_area_contents_page_containers)
        lbl_title.setGeometry(QRect(441, 10, 281, 16))
        lbl_title.setObjectName(CentralPageMakerStyle.lbl_title_style[0])
        lbl_title.setStyleSheet(CentralPageMakerStyle.lbl_title_style[1])
        vl_page_containers.addWidget(scroll_area_page_containers)
        scroll_area_page_containers.setWidget(scroll_area_contents_page_containers)
        page_containers_grid_layout.addWidget(scroll_area_page_containers, 0, 1, 1, 1)

        print(self.page_name)
