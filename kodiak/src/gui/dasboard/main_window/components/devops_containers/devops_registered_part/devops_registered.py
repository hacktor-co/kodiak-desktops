"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout,QHBoxLayout,
    QLabel, QFrame
)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)
from PyQt5.QtCore import (
    Qt, QSize,
    QRect, QCoreApplication
)

from commons.constants.app_paths import AppPaths
from .devops_registered_style import DevopsRegisteredStyles

class DevopsRegistered:

    def __init__(self):
        super(DevopsRegistered, self).__init__()
        
    def setup_ui(self, containers: QFrame):
        #----------------------------------------------------------------------registered_frame
        self.registered_frame = QFrame(containers)
        self.registered_frame.setGeometry(QRect(1, 95, 1162, 250))
        self.registered_frame.setStyleSheet("background-color: rgb(34,34,34);\n""border-radius:5px;")
        self.registered_frame.setFrameShape(QFrame.StyledPanel)
        self.registered_frame.setFrameShadow(QFrame.Raised)
        self.registered_frame.setObjectName("registered_frame")
        #----------------------------------------------------------------------vl_registered_frame
        self.vl_registered_frame = QVBoxLayout(self.registered_frame)
        self.vl_registered_frame.setContentsMargins(30, 30, 30, 30)
        self.vl_registered_frame.setObjectName("vl_registered_frame")
        #----------------------------------------------------------------------frame_containers_items_registered
        self.frame_containers_items_registered = QFrame(self.registered_frame)
        self.frame_containers_items_registered.setStyleSheet("")
        self.frame_containers_items_registered.setFrameShape(QFrame.StyledPanel)
        self.frame_containers_items_registered.setFrameShadow(QFrame.Raised)
        self.frame_containers_items_registered.setObjectName("frame_containers_items_registered")
        self.vl_registered_frame.addWidget(self.frame_containers_items_registered)

        from ..devops_part_box.details_box_devops import DetailsBoxDevops
        start_location = DetailsBoxDevops().create_deatailes_box(containers = self.frame_containers_items_registered, count_box = 1)

        end_location = DetailsBoxDevops().create_deatailes_box(
            containers = self.frame_containers_items_registered,
            count_box = 1, 
            box_type = False, 
            start_location = start_location
        )

        from ...devops_containers.boxs_devops_part.box_devops_part import BoxDevopsPart
        
        start_location = BoxDevopsPart().create_box(
            containers = self.frame_containers_items_registered,count_box = 1, 
            image=QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + 
            "/main_window/sy-mon-logo.svg" ),
             start_location = end_location
            )

        end_location = BoxDevopsPart().create_box(
            containers = self.frame_containers_items_registered,
            count_box = 2 ,
            title = "" ,
            box_type = False,
            start_location = start_location
            )

        del start_location
        del end_location

        self.frame_border_add_plugins_to_registered = QFrame(self.frame_containers_items_registered)
        self.frame_border_add_plugins_to_registered.setGeometry(QRect(830, 20, 138, 138))
        self.frame_border_add_plugins_to_registered.setCursor(QCursor(Qt.PointingHandCursor))

        self.frame_border_add_plugins_to_registered.setObjectName(
            DevopsRegisteredStyles.frame_border_add_plugins_to_registered_style[0]
        )
        self.frame_border_add_plugins_to_registered.setStyleSheet(
            DevopsRegisteredStyles.frame_border_add_plugins_to_registered_style[1]
            )
        self.frame_border_add_plugins_to_registered.setFrameShape(QFrame.StyledPanel)
        self.frame_border_add_plugins_to_registered.setFrameShadow(QFrame.Raised)
        #----------------------------------------------------------------------card_add_plugins_to_registered
        self.card_add_plugins_to_registered = QFrame(self.frame_border_add_plugins_to_registered)
        self.card_add_plugins_to_registered.setGeometry(QRect(3, 3, 133, 133))
        self.card_add_plugins_to_registered.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_add_plugins_to_registered.setObjectName(
            DevopsRegisteredStyles.card_add_plugins_to_registered_style[0]
        )
        self.card_add_plugins_to_registered.setStyleSheet(
            DevopsRegisteredStyles.card_add_plugins_to_registered_style[1]
        )
        self.card_add_plugins_to_registered.setFrameShape(QFrame.StyledPanel)
        self.card_add_plugins_to_registered.setFrameShadow(QFrame.Raised)
        
        #----------------------------------------------------------------------pic_add_plugin_to_registered
        self.pic_add_plugin_to_registered = QLabel(self.card_add_plugins_to_registered)
        self.pic_add_plugin_to_registered.setGeometry(QRect(0, 40, 131, 51))
        self.pic_add_plugin_to_registered.setObjectName(
            DevopsRegisteredStyles.pic_add_plugin_to_registered_style[0]
        )
        self.pic_add_plugin_to_registered.setStyleSheet(
            DevopsRegisteredStyles.pic_add_plugin_to_registered_style[1]
        )
        self.pic_add_plugin_to_registered.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + 
        "/main_window/add-plugin.svg"))
        self.pic_add_plugin_to_registered.setAlignment(Qt.AlignCenter)

