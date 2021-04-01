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
from .....components.primitive_box.box import Box as box_primitive

from typing import Any


class Registered:

    def __init__(self, form_base_layout: QFormLayout):
        super(Registered, self).__init__()
        self.form_base_layout: QFormLayout = form_base_layout

    def setup_ui(self, containers: QFrame, plugins: Any):
        # parent_unregistered_frame
        self.plugins = plugins
        self.parent_registered_frame = QFrame(containers)
        self.parent_registered_frame.setFrameShape(QFrame.StyledPanel)
        self.parent_registered_frame.setFrameShadow(QFrame.Raised)
        self.parent_registered_frame.setContentsMargins(0, 0, 0, 0)
        # parent_vl_unregistered_frame
        self.parent_vl_registered_frame = QVBoxLayout(self.parent_registered_frame)
        self.parent_vl_registered_frame.setContentsMargins(0, 0, 0, 0)
        self.parent_vl_registered_frame.setObjectName("vl_registered_frame")
        # registered_frame
        self.registered_frame = QFrame(self.parent_registered_frame)
        self.registered_frame.setMinimumSize(QSize(0, 500))
        self.registered_frame.setMaximumSize(QSize(16777215, 16777215))
        self.registered_frame.setObjectName(RegisteredStyles.registered_frame_style[0])
        self.registered_frame.setStyleSheet(RegisteredStyles.registered_frame_style[1])
        self.registered_frame.setFrameShape(QFrame.StyledPanel)
        self.registered_frame.setLayoutDirection(Qt.LeftToRight)
        self.registered_frame.setFrameShadow(QFrame.Raised)
        # vl_registered_frame
        self.vl_registered_frame = QVBoxLayout(self.registered_frame)
        self.vl_registered_frame.setContentsMargins(25, 25, 25, 25)
        self.vl_registered_frame.setObjectName("vl_registered_frame")
        # Add ScrollView
        self.scroll_area = QScrollArea(self.registered_frame)
        self.scroll_area.setObjectName(RegisteredStyles.scroll_area_style[0])
        self.scroll_area.setStyleSheet(RegisteredStyles.scroll_area_style[1])
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area_contents = QWidget()

        self.scroll_area_contents.setObjectName("scroll_area_contents_page_containers")
        # frame_containers_items_registered
        self.regestered_frame_gridLayout = QGridLayout(self.scroll_area_contents)
        self.regestered_frame_gridLayout.setSpacing(24)
        self.regestered_frame_gridLayout.setObjectName("regestered_frame_gridLayout")
        box_primitive().create_box(
            containers=self.scroll_area_contents,
            frame_gridLayout=self.regestered_frame_gridLayout, plugins=plugins
        )

        self.scroll_area.setWidget(self.scroll_area_contents)
        self.vl_registered_frame.addWidget(self.scroll_area)
        self.parent_vl_registered_frame.addWidget(self.registered_frame)
        self.form_base_layout.setWidget(1, QFormLayout.SpanningRole, self.parent_registered_frame)