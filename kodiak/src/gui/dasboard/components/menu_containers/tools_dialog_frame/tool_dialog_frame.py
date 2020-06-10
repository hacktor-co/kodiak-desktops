"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (QFrame, QLabel, QGridLayout)
from PyQt5.QtCore import (Qt, QRect, QPropertyAnimation)
from PyQt5.QtGui import (QPixmap, QCursor)

from commons.constants.app_paths import AppPaths
from .tool_dialog_frame_styles import ToolDialogFrameStyles
from .....utils.utils_clicked_event import UtilsClick

from functools import partial


class ToolDialogFrame:

    def __init__(self, containers: QFrame, page_containers_grid_layout: QGridLayout):
        super(ToolDialogFrame, self).__init__()
        self.containers = containers
        self.page_containers_grid_layout: QGridLayout = page_containers_grid_layout

        self.frame_tools = QFrame(self.containers)
        self.frame_tools.resize(91, 78)
        self.frame_tools.setStyleSheet(ToolDialogFrameStyles.all_frame_style)
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_tools.setObjectName("frame_tools")

        self.frame_concat_to_frame_tools = QFrame(self.containers)
        self.frame_concat_to_frame_tools.resize(481, 168)
        self.frame_concat_to_frame_tools.setStyleSheet(ToolDialogFrameStyles.all_frame_style)
        self.frame_concat_to_frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_tools.setObjectName("frame_concat_to_frame_tools")

    def setup_ui(self, page_containers: QFrame):

        self.lbl_tools = QLabel(self.frame_tools)
        self.lbl_tools.setText("Tools")
        self.lbl_tools.setGeometry(QRect(0, 27, 91, 21))
        self.lbl_tools.setStyleSheet(ToolDialogFrameStyles.lbl_frames_style)
        self.lbl_tools.setAlignment(Qt.AlignCenter)
        self.lbl_tools.setObjectName("lbl_tools")

        self.lbl_ellipse_tools = QLabel(self.frame_tools)
        self.lbl_ellipse_tools.setGeometry(QRect(0, 43, 91, 21))
        self.lbl_ellipse_tools.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.lbl_ellipse_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/ellipse_logo.svg"))
        self.lbl_ellipse_tools.setAlignment(Qt.AlignCenter)
        self.lbl_ellipse_tools.setObjectName("lbl_ellipse_tools")

        self.lbl_close_frame_tools = QLabel(self.frame_concat_to_frame_tools)
        self.lbl_close_frame_tools.setGeometry(QRect(5, 5, 21, 21))
        self.lbl_close_frame_tools.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_close_frame_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        self.lbl_close_frame_tools.setObjectName("lbl_close_frame_tools")

        self.card_forensic = QLabel(self.frame_concat_to_frame_tools)
        self.card_forensic.setText("Forensic")
        self.card_forensic.setGeometry(QRect(25, 25, 71, 46))
        self.card_forensic.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_forensic.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        self.card_forensic.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_forensic.setObjectName("card_forensic")

        self.pic_forensic = QLabel(self.frame_concat_to_frame_tools)
        self.pic_forensic.setGeometry(QRect(40, 10, 41, 31))
        self.pic_forensic.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_forensic.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_forensic.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/forensic_logo.svg"))
        self.pic_forensic.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_forensic.setObjectName("pic_forensic")

        self.card_lot = QLabel(self.frame_concat_to_frame_tools)
        self.card_lot.setText("lot")
        self.card_lot.setGeometry(QRect(112, 25, 71, 46))
        self.card_lot.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_lot.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        self.card_lot.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_lot.setObjectName("card_lot")

        self.pic_lot_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_lot_logo.setGeometry(QRect(126, 10, 41, 31))
        self.pic_lot_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_lot_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_lot_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/lot_logo.svg"))
        self.pic_lot_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_lot_logo.setObjectName("pic_lot_logo")

        self.card_network = QLabel(self.frame_concat_to_frame_tools)
        self.card_network.setGeometry(QRect(286, 25, 71, 46))
        self.card_network.setText("Network")
        self.card_network.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_network.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        self.card_network.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_network.setObjectName("card_network")

        self.pic_network_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_network_logo.setGeometry(QRect(300, 10, 41, 31))
        self.pic_network_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_network_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_network_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/network_logo.svg"))
        self.pic_network_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_network_logo.setObjectName("pic_network_logo")

        self.card_dev_ops = QLabel(self.frame_concat_to_frame_tools)
        self.card_dev_ops.setText("DevOps")
        self.card_dev_ops.setGeometry(QRect(199, 25, 71, 46))
        self.card_dev_ops.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_dev_ops.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        self.card_dev_ops.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_dev_ops.setObjectName("card_dev_ops")

        self.pic_dev_ops_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_dev_ops_logo.setGeometry(QRect(215, 10, 41, 31))
        self.pic_dev_ops_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_dev_ops_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_dev_ops_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/dev_ops_logo.svg"))
        self.pic_dev_ops_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_dev_ops_logo.setObjectName("pic_dev_ops_logo")

        self.card_monitoring = QLabel(self.frame_concat_to_frame_tools)
        self.card_monitoring.setText("Monitoring")
        self.card_monitoring.setGeometry(QRect(373, 105, 71, 46))
        self.card_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_monitoring.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        self.card_monitoring.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_monitoring.setObjectName("card_monitoring")

        self.pic_monitoring_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_monitoring_logo.setGeometry(QRect(388, 90, 41, 31))
        self.pic_monitoring_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_monitoring_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_monitoring_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/monitoring_logo.svg"))
        self.pic_monitoring_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_monitoring_logo.setObjectName("pic_monitoring_logo")

        self.card_web = QLabel(self.frame_concat_to_frame_tools)
        self.card_web.setText("Web")
        self.card_web.setGeometry(QRect(373, 25, 71, 46))
        self.card_web.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_web.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        self.card_web.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_web.setObjectName("card_web")

        self.pic_web_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_web_logo.setGeometry(QRect(388, 10, 41, 31))
        self.pic_web_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_web_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_web_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/web_logo.svg"))
        self.pic_web_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_web_logo.setObjectName("pic_web_logo")

        self.set_events(page_containers)

    def set_events(self, page_containers: QFrame):
        """this method for 

        Arguments:
            page_containers {QFrame} -- [description]
        """
        UtilsClick.clickable(self.lbl_close_frame_tools).connect(lambda: self.set_visibility_effect(True, False, True))

        UtilsClick.clickable(self.card_dev_ops).connect(partial(self.item_clicked, page_containers=page_containers))
        UtilsClick.clickable(self.card_web).connect(partial(self.item_clicked, page_containers=page_containers))
        UtilsClick.clickable(self.card_lot).connect(partial(self.item_clicked, page_containers=page_containers))
        UtilsClick.clickable(self.card_forensic).connect(partial(self.item_clicked, page_containers=page_containers))
        UtilsClick.clickable(self.card_monitoring).connect(partial(self.item_clicked, page_containers=page_containers))
        UtilsClick.clickable(self.card_network).connect(partial(self.item_clicked, page_containers=page_containers))

    def set_visibility_effect(self, visibility: bool, is_anime: bool, is_close: bool = False):
        """this method for set visibility  frame tools

        Arguments:
            visibility {bool} -- [this argument show status visibility frame ]
            is_anime {bool} -- [this argument show anime effect]

        Keyword Arguments:
            is_close {bool} -- [this argument when you want close frame] (default: {False})            
        """
        frame_tools_width: int = int(self.frame_tools.width() + 10)
        containers_width: int = int(self.containers.width())
        frame_concat_to_frame_tools_width: int = int(self.frame_concat_to_frame_tools.width() - 10)
        #
        x_location_frame_tools: int = int(containers_width - frame_tools_width)

        x_location_frame_tools_concat: int = int(
            containers_width - frame_concat_to_frame_tools_width - frame_tools_width)

        if visibility and is_anime:
            # start animation
            self.do_anim_frame_tools(self.frame_tools,
                                     QRect(x_location_frame_tools, 280, 91, 78)
                                     , QRect(x_location_frame_tools, 360, 91, 78))

            self.do_anim_concat_frame_tools(self.frame_concat_to_frame_tools,
                                            QRect(
                                                self.frame_tools.x() - 78,
                                                280, 161, 78),
                                            QRect(
                                                self.frame_tools.x() - frame_concat_to_frame_tools_width,
                                                360, 481, 168))

        if is_close:
            # click close button
            self.do_anim_frame_tools(self.frame_tools,
                                     QRect(x_location_frame_tools, 360, 91, 78)
                                     , QRect(x_location_frame_tools+containers_width, 360, 91, 78))

            self.do_anim_concat_frame_tools(self.frame_concat_to_frame_tools,
                                            QRect(x_location_frame_tools_concat, 360, 481, 78),
                                            QRect(x_location_frame_tools_concat+containers_width, 360, 481, 168))

        self.frame_tools.setVisible(visibility)
        self.frame_concat_to_frame_tools.setVisible(visibility)

        del frame_tools_width, frame_concat_to_frame_tools_width, containers_width
        del x_location_frame_tools, x_location_frame_tools_concat

    def do_anim_frame_tools(self, obj: QFrame, start_location: QRect, end_location: QRect):
        """ this method for do animation frame tools

            Arguments:
                obj {QFrame} -- [object must be do animation effect]
                start_location {QRect} -- [start location for anime]
                end_location {QRect} -- [end location for anime]
        """
        self.anim = QPropertyAnimation(obj, b"geometry")
        self.anim.setStartValue(start_location)
        self.anim.setEndValue(end_location)
        self.anim.start()

    def do_anim_concat_frame_tools(self, obj: QFrame, start_location: QRect, end_location: QRect):
        """ this method for do animation frame concat to frame tools tools

            Arguments:
                obj {QFrame} -- [object must be do animation effect]
                start_location {QRect} -- [start location for anime]
                end_location {QRect} -- [end location for anime]
        """

        self.anim_2 = QPropertyAnimation(obj, b"geometry")
        self.anim_2.setStartValue(start_location)
        self.anim_2.setEndValue(end_location)
        self.anim_2.start()

    def item_clicked(self, page_containers: QFrame):
        """ this method when call client push devops item

            Arguments:
                page_containers {QFrame} -- [devops layout in this layer ]78
        """
        from ...central_page_maker.central_page_maker import CentralPageMaker
        # Delete Children in Parent

        CentralPageMaker(containers=page_containers, page_containers_grid_layout=self.page_containers_grid_layout)
        self.set_visibility_effect(True, False, True)
