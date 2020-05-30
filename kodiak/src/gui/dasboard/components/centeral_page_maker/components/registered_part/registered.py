"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout,QHBoxLayout,
    QLabel, QFrame,
    QGridLayout, QWidget,
    QScrollArea, QDesktopWidget
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

from .registered_style import RegisteredStyles

class Registered:

    def __init__(self):
        super(Registered, self).__init__()
        
    def setup_ui(self, containers: QFrame):
        #registered_frame
        self.registered_frame = QFrame(containers)
        if QDesktopWidget().geometry().height()<800:
            self.registered_frame.setGeometry(QRect((containers.width()-900)/2, 10, 900, 250))
        else:
            self.registered_frame.setGeometry(QRect((containers.width()-900)/2, 25, 900, 250))
        
        self.registered_frame.setStyleSheet("background-color: rgb(34,34,34);\n""border-radius:5px;")
        self.registered_frame.setFrameShape(QFrame.StyledPanel)
        self.registered_frame.setFrameShadow(QFrame.Raised)
        self.registered_frame.setObjectName("registered_frame")
        #vl_registered_frame
        self.vl_registered_frame = QVBoxLayout(self.registered_frame)
        self.vl_registered_frame.setContentsMargins(30, 30, 30, 30)
        self.vl_registered_frame.setObjectName("vl_registered_frame")
        #Add ScrollView
        self.scrollArea = QScrollArea(self.registered_frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1080, 344))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #Add Vlayout ScroolView
        self.vlayout_scroll_view = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vlayout_scroll_view.setObjectName("verticalLayout_3")
        #frame_containers_items_registered
        self.frame_containers_items_registered = QFrame(self.scrollAreaWidgetContents)
        self.frame_containers_items_registered.setFrameShape(QFrame.StyledPanel)
        self.frame_containers_items_registered.setFrameShadow(QFrame.Raised)
        self.frame_containers_items_registered.setObjectName("frame_containers_items_registered")
        self.vl_registered_frame.addWidget(self.frame_containers_items_registered)

        self.regestered_frame_gridLayout = QGridLayout(self.frame_containers_items_registered)
        self.regestered_frame_gridLayout.setSpacing(24)
        self.regestered_frame_gridLayout.setObjectName("regestered_frame_gridLayout")
        from .....components.primitive_box.box import Box as box_primitive

        #start_location = 
        
        start_index = box_primitive().create_box(
            containers = self.frame_containers_items_registered, count_box = 2,
            frame_gridLayout = self.regestered_frame_gridLayout
        )
        box_primitive().create_box(
            containers = self.frame_containers_items_registered, count_box = 3,
            start_index= start_index,frame_gridLayout = self.regestered_frame_gridLayout,
            box_type = False
            )
        
        del start_index

        self.vlayout_scroll_view.addWidget(self.frame_containers_items_registered, 0, Qt.AlignLeft)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.vl_registered_frame.addWidget(self.scrollArea)
      
        # self.frame_border_add_plugins_to_registered = QFrame(self.frame_containers_items_registered)
        # self.frame_border_add_plugins_to_registered.setGeometry(QRect(830, 20, 138, 138))
        # self.frame_border_add_plugins_to_registered.setCursor(QCursor(Qt.PointingHandCursor))

        # self.frame_border_add_plugins_to_registered.setObjectName(
        #     RegisteredStyles.frame_border_add_plugins_to_registered_style[0]
        # )
        # self.frame_border_add_plugins_to_registered.setStyleSheet(
        #     RegisteredStyles.frame_border_add_plugins_to_registered_style[1]
        #     )
        # self.frame_border_add_plugins_to_registered.setFrameShape(QFrame.StyledPanel)
        # self.frame_border_add_plugins_to_registered.setFrameShadow(QFrame.Raised)
        # #----------------------------------------------------------------------card_add_plugins_to_registered
        # self.card_add_plugins_to_registered = QFrame(self.frame_border_add_plugins_to_registered)
        # self.card_add_plugins_to_registered.setGeometry(QRect(3, 3, 133, 133))
        # self.card_add_plugins_to_registered.setCursor(QCursor(Qt.PointingHandCursor))
        # self.card_add_plugins_to_registered.setObjectName(
        #     RegisteredStyles.card_add_plugins_to_registered_style[0]
        # )
        # self.card_add_plugins_to_registered.setStyleSheet(
        #     RegisteredStyles.card_add_plugins_to_registered_style[1]
        # )
        # self.card_add_plugins_to_registered.setFrameShape(QFrame.StyledPanel)
        # self.card_add_plugins_to_registered.setFrameShadow(QFrame.Raised)
        
        # #----------------------------------------------------------------------pic_add_plugin_to_registered
        # self.pic_add_plugin_to_registered = QLabel(self.card_add_plugins_to_registered)
        # self.pic_add_plugin_to_registered.setGeometry(QRect(0, 40, 131, 51))
        # self.pic_add_plugin_to_registered.setObjectName(
        #     RegisteredStyles.pic_add_plugin_to_registered_style[0]
        # )
        # self.pic_add_plugin_to_registered.setStyleSheet(
        #     RegisteredStyles.pic_add_plugin_to_registered_style[1]
        # )
        # self.pic_add_plugin_to_registered.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + 
        # "/main_window/add-plugin.svg"))
        # self.pic_add_plugin_to_registered.setAlignment(Qt.AlignCenter)

