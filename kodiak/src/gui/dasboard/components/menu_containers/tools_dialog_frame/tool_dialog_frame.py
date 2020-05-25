"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (QFrame, QLabel)
from PyQt5.QtCore import (Qt, QRect, QPropertyAnimation)
from PyQt5.QtGui import (QPixmap, QCursor)

from commons.constants.app_paths import AppPaths
from .tool_dialog_frame_styles import ToolDialogFrameStyles
from .....utils.utils_clicked_event import UtilsClick

from functools import partial


class ToolDialogFrame:

    def __init__(self, containers: QFrame):
        super(ToolDialogFrame, self).__init__()

        self.frame_tools = QFrame(containers)
        self.frame_tools.setGeometry(QRect(1240, 360, 91, 78))
        self.frame_tools.setStyleSheet(ToolDialogFrameStyles.all_frame_style)
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_tools.setObjectName("frame_tools")

        self.frame_concat_to_frame_tools = QFrame(containers)
        self.frame_concat_to_frame_tools.setGeometry(QRect(770, 360, 481, 168))
        self.frame_concat_to_frame_tools.setStyleSheet(ToolDialogFrameStyles.all_frame_style)
        self.frame_concat_to_frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_tools.setObjectName("frame_concat_to_frame_tools")

    def setup_ui(self, containers_item: QFrame):

        lbl_tools = QLabel(self.frame_tools)
        lbl_tools.setText("Tools")
        lbl_tools.setGeometry(QRect(0, 27, 91, 21))
        lbl_tools.setStyleSheet(ToolDialogFrameStyles.lbl_frames_style)
        lbl_tools.setAlignment(Qt.AlignCenter)
        lbl_tools.setObjectName("lbl_tools")

        lbl_ellipse_tools = QLabel(self.frame_tools)
        lbl_ellipse_tools.setGeometry(QRect(0, 43, 91, 21))
        lbl_ellipse_tools.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        lbl_ellipse_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/ellipse_logo.svg"))
        lbl_ellipse_tools.setAlignment(Qt.AlignCenter)
        lbl_ellipse_tools.setObjectName("lbl_ellipse_tools")

        lbl_close_frame_tools = QLabel(self.frame_concat_to_frame_tools)
        lbl_close_frame_tools.setGeometry(QRect(5, 5, 21, 21))
        lbl_close_frame_tools.setCursor(QCursor(Qt.PointingHandCursor))
        lbl_close_frame_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        lbl_close_frame_tools.setObjectName("lbl_close_frame_tools")
        UtilsClick.clickable(lbl_close_frame_tools).connect(lambda: self.set_visibility_effect(True, False, True))

        card_forensic = QLabel(self.frame_concat_to_frame_tools)
        card_forensic.setText("Forensic")
        card_forensic.setGeometry(QRect(25, 25, 71, 46))
        card_forensic.setCursor(QCursor(Qt.PointingHandCursor))
        card_forensic.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        card_forensic.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        card_forensic.setObjectName("card_forensic")

        pic_forensic = QLabel(self.frame_concat_to_frame_tools)
        pic_forensic.setGeometry(QRect(40, 10, 41, 31))
        pic_forensic.setCursor(QCursor(Qt.PointingHandCursor))
        pic_forensic.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        pic_forensic.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/forensic_logo.svg"))
        pic_forensic.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        pic_forensic.setObjectName("pic_forensic")

        card_lot = QLabel(self.frame_concat_to_frame_tools)
        card_lot.setText("lot")
        card_lot.setGeometry(QRect(112, 25, 71, 46))
        card_lot.setCursor(QCursor(Qt.PointingHandCursor))
        card_lot.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        card_lot.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        card_lot.setObjectName("card_lot")

        pic_lot_logo = QLabel(self.frame_concat_to_frame_tools)
        pic_lot_logo.setGeometry(QRect(126, 10, 41, 31))
        pic_lot_logo.setCursor(QCursor(Qt.PointingHandCursor))
        pic_lot_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        pic_lot_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/lot_logo.svg"))
        pic_lot_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        pic_lot_logo.setObjectName("pic_lot_logo")

        card_network = QLabel(self.frame_concat_to_frame_tools)
        card_network.setGeometry(QRect(286, 25, 71, 46))
        card_network.setText("Network")
        card_network.setCursor(QCursor(Qt.PointingHandCursor))
        card_network.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        card_network.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        card_network.setObjectName("card_network")

        pic_network_logo = QLabel(self.frame_concat_to_frame_tools)
        pic_network_logo.setGeometry(QRect(300, 10, 41, 31))
        pic_network_logo.setCursor(QCursor(Qt.PointingHandCursor))
        pic_network_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        pic_network_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/network_logo.svg"))
        pic_network_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        pic_network_logo.setObjectName("pic_network_logo")

        card_dev_ops = QLabel(self.frame_concat_to_frame_tools)
        card_dev_ops.setText("DevOps")
        card_dev_ops.setGeometry(QRect(199, 25, 71, 46))
        card_dev_ops.setCursor(QCursor(Qt.PointingHandCursor))
        card_dev_ops.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        card_dev_ops.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        card_dev_ops.setObjectName("card_dev_ops")
        UtilsClick.clickable(card_dev_ops).connect(partial(self.devops_clicked, containers_item=containers_item))

        pic_dev_ops_logo = QLabel(self.frame_concat_to_frame_tools)
        pic_dev_ops_logo.setGeometry(QRect(215, 10, 41, 31))
        pic_dev_ops_logo.setCursor(QCursor(Qt.PointingHandCursor))
        pic_dev_ops_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        pic_dev_ops_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/dev_ops_logo.svg"))
        pic_dev_ops_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        pic_dev_ops_logo.setObjectName("pic_dev_ops_logo")

        card_monitoring = QLabel(self.frame_concat_to_frame_tools)
        card_monitoring.setText("Monitoring")
        card_monitoring.setGeometry(QRect(373, 105, 71, 46))
        card_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        card_monitoring.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        card_monitoring.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        card_monitoring.setObjectName("card_monitoring")

        pic_monitoring_logo = QLabel(self.frame_concat_to_frame_tools)
        pic_monitoring_logo.setGeometry(QRect(388, 90, 41, 31))
        pic_monitoring_logo.setCursor(QCursor(Qt.PointingHandCursor))
        pic_monitoring_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        pic_monitoring_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/monitoring_logo.svg"))
        pic_monitoring_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        pic_monitoring_logo.setObjectName("pic_monitoring_logo")

        card_web = QLabel(self.frame_concat_to_frame_tools)
        card_web.setText("Web")
        card_web.setGeometry(QRect(373, 25, 71, 46))
        card_web.setCursor(QCursor(Qt.PointingHandCursor))
        card_web.setStyleSheet(ToolDialogFrameStyles.cards_in_frame_style)
        card_web.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        card_web.setObjectName("card_web")

        pic_web_logo = QLabel(self.frame_concat_to_frame_tools)
        pic_web_logo.setGeometry(QRect(388, 10, 41, 31))
        pic_web_logo.setCursor(QCursor(Qt.PointingHandCursor))
        pic_web_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        pic_web_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/web_logo.svg"))
        pic_web_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        pic_web_logo.setObjectName("pic_web_logo")

    def set_visibility_effect(self, visibility: bool, is_anime: bool, is_close: bool = False):
        """this method for set visibility  frame tools

        Arguments:
            visibility {bool} -- [this argument show status visibility frame ]
            is_anime {bool} -- [this argument show anime effect]

        Keyword Arguments:
            is_close {bool} -- [this argument when you want close frame] (default: {False})            
        """

        if visibility and is_anime:
            self.do_anim_frame_tools(self.frame_tools, QRect(1240, 280, 91, 78), QRect(1240, 360, 91, 78))
            self.do_anim_concat_frame_tools(self.frame_concat_to_frame_tools, QRect(1120, 280, 161, 78),
                                            QRect(770, 360, 481, 168))

        if is_close:
            self.do_anim_frame_tools(self.frame_tools, QRect(1240, 360, 91, 78), QRect(1440, 360, 91, 78))
            self.do_anim_concat_frame_tools(self.frame_concat_to_frame_tools, QRect(1120, 360, 161, 78),
                                            QRect(1420, 360, 161, 78))

        self.frame_tools.setVisible(visibility)
        self.frame_concat_to_frame_tools.setVisible(visibility)

    def do_anim_frame_tools(self, obj: QFrame, start_location: QRect, end_location: QRect):
        """ this method for do animation frame tools

            Arguments:
                obj {QFrame} -- [object must be do animation effect]
                start_location {QRect} -- [start location for anime]
                end_location {QRect} -- [end location for anime]
        """
        self.anim = QPropertyAnimation(obj, b"geometry")
        self.anim.setDuration(150)
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
        self.anim_2.setDuration(150)
        self.anim_2.setStartValue(start_location)
        self.anim_2.setEndValue(end_location)
        self.anim_2.start()

    def devops_clicked(self, containers_item: QFrame):
        """ this method when call client push devops item

            Arguments:
                containers_item {QFrame} -- [devops layout in this layer ]
        """
        # from ....main_window.components.devops_containers.devops_containers import DevopsContainers
        # self.devops = DevopsContainers()
        from ...centeral_page_maker.centeral_page_maker import CenteralPageMaker
        CenteralPageMaker(containers_item)
        # self.devops.setup_ui(containers=containers_item)
        # self.devops.set_visibility_effect(True)
        # self.set_visibility_effect(True, False, True)
