"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QFrame,
    QGridLayout, QWidget,
    QScrollArea, QFormLayout,
    QLabel
)
from PyQt5.QtCore import (
    Qt, QRect, QSize
)

from .registered_style import RegisteredStyles


class Registered:

    def __init__(self, form_base_layout: QFormLayout):
        super(Registered, self).__init__()

        self.form_base_layout: QFormLayout = form_base_layout

    def setup_ui(self, containers: QFrame):
        # parent_unregistered_frame
        self.parent_registered_frame = QFrame(containers)
        self.parent_registered_frame.setFrameShape(QFrame.StyledPanel)
        self.parent_registered_frame.setFrameShadow(QFrame.Raised)
        self.parent_registered_frame.setContentsMargins(0, 45, 0, 0)
        # parent_vl_unregistered_frame
        self.parent_vl_registered_frame = QVBoxLayout(self.parent_registered_frame)
        self.parent_vl_registered_frame.setContentsMargins(30, 30, 30, 30)
        self.parent_vl_registered_frame.setObjectName("vl_registered_frame")
        # registered_frame
        self.registered_frame = QFrame(self.parent_registered_frame)
        self.registered_frame.setMinimumSize(QSize(0, 250))
        self.registered_frame.setMaximumSize(QSize(16777215, 350))
        self.registered_frame.setObjectName(RegisteredStyles.registered_frame_style[0])
        self.registered_frame.setStyleSheet(RegisteredStyles.registered_frame_style[1])
        self.registered_frame.setFrameShape(QFrame.StyledPanel)
        self.registered_frame.setLayoutDirection(Qt.LeftToRight)
        self.registered_frame.setFrameShadow(QFrame.Raised)
        # vl_registered_frame
        self.vl_registered_frame = QVBoxLayout(self.registered_frame)
        self.vl_registered_frame.setContentsMargins(30, 30, 30, 30)
        self.vl_registered_frame.setObjectName("vl_registered_frame")
        # Add ScrollView
        self.scroll_area = QScrollArea(self.registered_frame)
        self.scroll_area.setObjectName(RegisteredStyles.scroll_area_style[0])
        self.scroll_area.setStyleSheet(RegisteredStyles.scroll_area_style[1])
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setGeometry(QRect(0, 0, 1080, 344))
        self.scroll_area_contents.setObjectName("scroll_area_contents_page_containers")
        # Add Vlayout ScroolView
        self.vlayout_scroll_view = QVBoxLayout(self.scroll_area_contents)
        self.vlayout_scroll_view.setObjectName("vlayout_scroll_view")
        # frame_containers_items_registered
        self.frame_containers_items_registered = QFrame(self.scroll_area_contents)
        self.frame_containers_items_registered.setFrameShape(QFrame.StyledPanel)
        self.frame_containers_items_registered.setFrameShadow(QFrame.Raised)
        self.frame_containers_items_registered.setObjectName("frame_containers_items_registered")
        self.vl_registered_frame.addWidget(self.frame_containers_items_registered)

        self.regestered_frame_gridLayout = QGridLayout(self.frame_containers_items_registered)
        self.regestered_frame_gridLayout.setSpacing(24)
        self.regestered_frame_gridLayout.setObjectName("regestered_frame_gridLayout")

        # lbl_registered
        self.lbl_registered = QLabel(self.parent_registered_frame)
        self.lbl_registered.setGeometry(QRect(75, 15, 141, 32))

        self.lbl_registered.setMinimumSize(QSize(91, 32))
        self.lbl_registered.setObjectName(RegisteredStyles.lbl_registered_style[0])
        self.lbl_registered.setStyleSheet(RegisteredStyles.lbl_registered_style[1])
        self.lbl_registered.setAlignment(Qt.AlignCenter)
        self.lbl_registered.setText("REGISTERED")

        from ....components.primitive_box.box import Box as box_primitive

        start_index = box_primitive().create_box(
            containers=self.frame_containers_items_registered, count_box=1,
            frame_gridLayout=self.regestered_frame_gridLayout
        )
        # box_primitive().create_box(
        #     containers=self.frame_containers_items_registered, count_box=5,
        #     start_index=start_index, frame_gridLayout=self.regestered_frame_gridLayout,
        #     box_type=False
        # )

        del start_index

        self.vlayout_scroll_view.addWidget(self.frame_containers_items_registered, 0, Qt.AlignLeft)
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.vl_registered_frame.addWidget(self.scroll_area)
        self.parent_vl_registered_frame.addWidget(self.registered_frame)
        self.form_base_layout.setWidget(1, QFormLayout.SpanningRole, self.parent_registered_frame)

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
