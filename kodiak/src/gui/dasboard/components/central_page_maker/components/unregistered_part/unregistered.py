"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QFrame,
    QGridLayout, QScrollArea,
    QWidget, QFormLayout,
    QLabel
)

from PyQt5.QtCore import (Qt, QRect, QSize)

from .unregistered_style import UnregisteredStyles


class Unregistered:

    def __init__(self, form_base_layout: QFormLayout):
        super(Unregistered, self).__init__()

        self.form_base_layout: QFormLayout = form_base_layout

    def setup_ui(self, containers: QFrame):
        # parent_unregistered_frame
        self.parent_unregistered_frame = QFrame(containers)
        self.parent_unregistered_frame.setFrameShape(QFrame.StyledPanel)
        self.parent_unregistered_frame.setFrameShadow(QFrame.Raised)
        self.parent_unregistered_frame.setContentsMargins(0, 45, 0, 0)
        # parent_vl_unregistered_frame
        self.parent_vl_unregistered_frame = QVBoxLayout(self.parent_unregistered_frame)
        self.parent_vl_unregistered_frame.setContentsMargins(30, 30, 30, 30)
        self.parent_vl_unregistered_frame.setObjectName("vl_registered_frame")
        # unregistered_frame
        self.unregistered_frame = QFrame(self.parent_unregistered_frame)
        self.unregistered_frame.setMinimumSize(QSize(0, 250))
        self.unregistered_frame.setMaximumSize(QSize(16777215, 350))
        self.unregistered_frame.setObjectName(UnregisteredStyles.unregistered_frame_style[0])
        self.unregistered_frame.setStyleSheet(UnregisteredStyles.unregistered_frame_style[1])
        self.unregistered_frame.setFrameShape(QFrame.StyledPanel)
        self.unregistered_frame.setLayoutDirection(Qt.LeftToRight)
        self.unregistered_frame.setFrameShadow(QFrame.Raised)
        # vl_unregistered_frame
        self.vl_unregistered_frame = QVBoxLayout(self.unregistered_frame)
        self.vl_unregistered_frame.setContentsMargins(30, 30, 30, 30)
        self.vl_unregistered_frame.setObjectName("vl_unregistered_frame")
        # Add ScrollView
        self.scroll_area = QScrollArea(self.unregistered_frame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName(UnregisteredStyles.scroll_area_style[0])
        self.scroll_area.setStyleSheet(UnregisteredStyles.scroll_area_style[1])
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setGeometry(QRect(0, 0, 1080, 344))
        self.scroll_area_contents.setObjectName("scroll_area_contents_page_containers")
        # Add Vlayout ScroolView
        self.vlayout_scroll_view = QVBoxLayout(self.scroll_area_contents)
        self.vlayout_scroll_view.setObjectName("verticalLayout_3")
        # frame_containers_items_unregistered
        self.frame_containers_items_unregistered = QFrame(self.unregistered_frame)
        self.frame_containers_items_unregistered.setStyleSheet("")
        self.frame_containers_items_unregistered.setFrameShape(QFrame.StyledPanel)
        self.frame_containers_items_unregistered.setFrameShadow(QFrame.Raised)
        self.frame_containers_items_unregistered.setObjectName("frame_containers_items_unregistered")
        self.vl_unregistered_frame.addWidget(self.frame_containers_items_unregistered)
        # unregestered_frame_gridLayout
        self.unregestered_frame_gridLayout = QGridLayout(self.frame_containers_items_unregistered)
        self.unregestered_frame_gridLayout.setSpacing(24)
        self.unregestered_frame_gridLayout.setObjectName("unregestered_frame_gridLayout")

        # lbl_unregistered
        self.lbl_unregistered = QLabel(self.parent_unregistered_frame)
        self.lbl_unregistered.setGeometry(QRect(75, 15, 141, 32))
        self.lbl_unregistered.setMinimumSize(QSize(91, 32))
        self.lbl_unregistered.setObjectName(UnregisteredStyles.lbl_unregistered_style[0])
        self.lbl_unregistered.setStyleSheet(UnregisteredStyles.lbl_unregistered_style[1])
        self.lbl_unregistered.setAlignment(Qt.AlignCenter)
        self.lbl_unregistered.setText("UNREGISTERED")

        from .....components.primitive_box.box import Box as box_primitive

        start_index = box_primitive().create_box(
            containers=self.frame_containers_items_unregistered, count_box=10,
            frame_gridLayout=self.unregestered_frame_gridLayout
        )
        box_primitive().create_box(
            containers=self.frame_containers_items_unregistered, count_box=5,
            start_index=start_index, frame_gridLayout=self.unregestered_frame_gridLayout,
            box_type=False
        )

        del start_index

        self.vlayout_scroll_view.addWidget(self.frame_containers_items_unregistered, 0, Qt.AlignLeft)
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.vl_unregistered_frame.addWidget(self.scroll_area)
        self.parent_vl_unregistered_frame.addWidget(self.unregistered_frame)
        self.form_base_layout.setWidget(2, QFormLayout.SpanningRole, self.parent_unregistered_frame)

        # start_location = box_primitive().create_box(
        #     containers = self.frame_containers_items_unregistered,count_box = 1, 
        #     box_type = False
        #     )

        # end_location = box_primitive().create_box(
        #     containers = self.frame_containers_items_unregistered,count_box = 1, 
        #     start_location= start_location
        #     )

        # start_location = box_primitive().create_box(
        #     containers = self.frame_containers_items_unregistered,
        #     count_box = 2 ,
        #     box_type = False,
        #     start_location = end_location
        #     )

        # del start_location
        # del end_location

        # self.frame_border_add_plugins_to_unregistered = QFrame(self.frame_containers_items_unregistered)
        # self.frame_border_add_plugins_to_unregistered.setGeometry(QRect(670, 20, 138, 138))
        # self.frame_border_add_plugins_to_unregistered.setCursor(QCursor(Qt.PointingHandCursor))

        # self.frame_border_add_plugins_to_unregistered.setObjectName(
        #     UnregisteredStyles.frame_border_add_plugins_to_registered_style[0]
        # )
        # self.frame_border_add_plugins_to_unregistered.setStyleSheet(
        #     UnregisteredStyles.frame_border_add_plugins_to_registered_style[1]
        #     )
        # self.frame_border_add_plugins_to_unregistered.setFrameShape(QFrame.StyledPanel)
        # self.frame_border_add_plugins_to_unregistered.setFrameShadow(QFrame.Raised)
        # #----------------------------------------------------------------------card_add_plugins_to_unregistered
        # self.card_add_plugins_to_unregistered = QFrame(self.frame_border_add_plugins_to_unregistered)
        # self.card_add_plugins_to_unregistered.setGeometry(QRect(3, 3, 133, 133))
        # self.card_add_plugins_to_unregistered.setCursor(QCursor(Qt.PointingHandCursor))
        # self.card_add_plugins_to_unregistered.setObjectName(
        #     UnregisteredStyles.card_add_plugins_to_registered_style[0]
        # )
        # self.card_add_plugins_to_unregistered.setStyleSheet(
        #     UnregisteredStyles.card_add_plugins_to_registered_style[1]
        # )
        # self.card_add_plugins_to_unregistered.setFrameShape(QFrame.StyledPanel)
        # self.card_add_plugins_to_unregistered.setFrameShadow(QFrame.Raised)

        # #----------------------------------------------------------------------pic_add_plugin_to_unregistered
        # self.pic_add_plugin_to_unregistered = QLabel(self.card_add_plugins_to_unregistered)
        # self.pic_add_plugin_to_unregistered.setGeometry(QRect(0, 40, 131, 51))
        # self.pic_add_plugin_to_unregistered.setObjectName(
        #     UnregisteredStyles.pic_add_plugin_to_registered_style[0]
        # )
        # self.pic_add_plugin_to_unregistered.setStyleSheet(
        #     UnregisteredStyles.pic_add_plugin_to_registered_style[1]
        # )
        # self.pic_add_plugin_to_unregistered.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + 
        # "/main_window/add-plugin.svg"))
        # self.pic_add_plugin_to_unregistered.setAlignment(Qt.AlignCenter)
