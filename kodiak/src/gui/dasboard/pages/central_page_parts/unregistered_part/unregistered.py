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

from .unregistered_style import UnregisteredStyles
class Unregistered:

    def __init__(self):
        super(Unregistered, self).__init__()

    def setup_ui(self, containers: QFrame):
        #----------------------------------------------------------------------unregistered_frame
        self.unregistered_frame = QFrame(containers)
        self.unregistered_frame.setGeometry(QRect(1, 440, 1162, 250))
        self.unregistered_frame.setStyleSheet("background-color: rgb(34,34,34);\n""border-radius:5px;\n""")
        self.unregistered_frame.setFrameShape(QFrame.StyledPanel)
        self.unregistered_frame.setFrameShadow(QFrame.Raised)
        self.unregistered_frame.setObjectName("unregistered_frame")
        #----------------------------------------------------------------------vl_unregistered_frame
        self.vl_unregistered_frame = QVBoxLayout(self.unregistered_frame)
        self.vl_unregistered_frame.setContentsMargins(30, 30, 30, 30)
        self.vl_unregistered_frame.setObjectName("vl_unregistered_frame")
        #----------------------------------------------------------------------frame_containers_items_unregistered
        self.frame_containers_items_unregistered = QFrame(self.unregistered_frame)
        self.frame_containers_items_unregistered.setStyleSheet("")
        self.frame_containers_items_unregistered.setFrameShape(QFrame.StyledPanel)
        self.frame_containers_items_unregistered.setFrameShadow(QFrame.Raised)
        self.frame_containers_items_unregistered.setObjectName("frame_containers_items_unregistered")
        self.vl_unregistered_frame.addWidget(self.frame_containers_items_unregistered)

        from ....components.box_mode1.box import Box as box_mode1
        
        start_location = box_mode1().create_box(
            containers = self.frame_containers_items_unregistered,count_box = 1, 
            box_type = False
            )
            
        end_location = box_mode1().create_box(
            containers = self.frame_containers_items_unregistered,count_box = 1, 
            start_location= start_location
            )

        start_location = box_mode1().create_box(
            containers = self.frame_containers_items_unregistered,
            count_box = 2 ,
            box_type = False,
            start_location = end_location
            )

        del start_location
        del end_location

        self.frame_border_add_plugins_to_unregistered = QFrame(self.frame_containers_items_unregistered)
        self.frame_border_add_plugins_to_unregistered.setGeometry(QRect(670, 20, 138, 138))
        self.frame_border_add_plugins_to_unregistered.setCursor(QCursor(Qt.PointingHandCursor))

        self.frame_border_add_plugins_to_unregistered.setObjectName(
            UnregisteredStyles.frame_border_add_plugins_to_registered_style[0]
        )
        self.frame_border_add_plugins_to_unregistered.setStyleSheet(
            UnregisteredStyles.frame_border_add_plugins_to_registered_style[1]
            )
        self.frame_border_add_plugins_to_unregistered.setFrameShape(QFrame.StyledPanel)
        self.frame_border_add_plugins_to_unregistered.setFrameShadow(QFrame.Raised)
        #----------------------------------------------------------------------card_add_plugins_to_unregistered
        self.card_add_plugins_to_unregistered = QFrame(self.frame_border_add_plugins_to_unregistered)
        self.card_add_plugins_to_unregistered.setGeometry(QRect(3, 3, 133, 133))
        self.card_add_plugins_to_unregistered.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_add_plugins_to_unregistered.setObjectName(
            UnregisteredStyles.card_add_plugins_to_registered_style[0]
        )
        self.card_add_plugins_to_unregistered.setStyleSheet(
            UnregisteredStyles.card_add_plugins_to_registered_style[1]
        )
        self.card_add_plugins_to_unregistered.setFrameShape(QFrame.StyledPanel)
        self.card_add_plugins_to_unregistered.setFrameShadow(QFrame.Raised)
        
        #----------------------------------------------------------------------pic_add_plugin_to_unregistered
        self.pic_add_plugin_to_unregistered = QLabel(self.card_add_plugins_to_unregistered)
        self.pic_add_plugin_to_unregistered.setGeometry(QRect(0, 40, 131, 51))
        self.pic_add_plugin_to_unregistered.setObjectName(
            UnregisteredStyles.pic_add_plugin_to_registered_style[0]
        )
        self.pic_add_plugin_to_unregistered.setStyleSheet(
            UnregisteredStyles.pic_add_plugin_to_registered_style[1]
        )
        self.pic_add_plugin_to_unregistered.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + 
        "/main_window/add-plugin.svg"))
        self.pic_add_plugin_to_unregistered.setAlignment(Qt.AlignCenter)

