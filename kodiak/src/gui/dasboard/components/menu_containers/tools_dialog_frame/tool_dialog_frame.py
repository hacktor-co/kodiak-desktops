"""

"""

from PyQt5.QtWidgets import (QFrame, QLabel)
from PyQt5.QtCore import (Qt, QRect, QPropertyAnimation)
from PyQt5.QtGui import (QIcon, QPixmap, QCursor)

from commons.constants.app_paths import AppPaths
from .tool_dialog_frame_styles import ToolDialogFrameStyles
from  .....utils.utils_clicked_event import UtilsClick

class ToolDialogFrame:

    def __init__(self):
        super(ToolDialogFrame, self).__init__()

    def setup_ui(self, containers: QFrame):

        self.frame_tools = QFrame(containers)
        self.frame_tools.setGeometry(QRect(1240, 360, 91, 78))
        self.frame_tools.setStyleSheet(ToolDialogFrameStyles.all_frame_style)
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_tools.setObjectName("frame_tools")

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
        self.frame_concat_to_frame_tools = QFrame(containers)
        self.frame_concat_to_frame_tools.setGeometry(QRect(770, 360, 481, 168))
        self.frame_concat_to_frame_tools.setStyleSheet(ToolDialogFrameStyles.all_frame_style)
        self.frame_concat_to_frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_tools.setObjectName("frame_concat_to_frame_tools")
        self.lbl_close_frame_tools = QLabel(self.frame_concat_to_frame_tools)
        self.lbl_close_frame_tools.setGeometry(QRect(5, 5, 21, 21))
        self.lbl_close_frame_tools.setCursor(QCursor(Qt.PointingHandCursor))

        self.lbl_close_frame_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        self.lbl_close_frame_tools.setObjectName("lbl_close_frame_tools")
        UtilsClick.clickable(self.lbl_close_frame_tools).connect(lambda : self.set_visibility_effect(True, False, True))

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

        self.pic_Network_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_Network_logo.setGeometry(QRect(300, 10, 41, 31))
        self.pic_Network_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_Network_logo.setStyleSheet(ToolDialogFrameStyles.transparent_color_style)
        self.pic_Network_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/network_logo.svg"))
        self.pic_Network_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_Network_logo.setObjectName("pic_Network_logo")

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

    def set_visibility_effect(self, visibility: bool,is_anime: bool, is_close: bool = False ):
        """this method for set visibility  frame tools

        Arguments:
            visibility {bool} -- [this argument show status visibility frame ]
            is_anime {bool} -- [this argument show anime effect]

        Keyword Arguments:
            is_close {bool} -- [this argument when you want close frame] (default: {False})            
        """

        if visibility and is_anime:
            self.do_anim_frame_tools(self.frame_tools,QRect(1240, 280, 91, 78),QRect(1240, 360, 91, 78))
            self.do_anim_concat_frame_tools(self.frame_concat_to_frame_tools, QRect(1120, 280, 161, 78), QRect(770, 360, 481, 168))
        
        if is_close:
            self.do_anim_frame_tools(self.frame_tools,QRect(1240, 360, 91, 78),QRect(1440, 360, 91, 78))
            self.do_anim_concat_frame_tools(self.frame_concat_to_frame_tools, QRect(1120, 360, 161, 78), QRect(1420, 360, 161, 78))
    
        self.frame_tools.setVisible(visibility)
        self.frame_concat_to_frame_tools.setVisible(visibility)

    def do_anim_frame_tools(self, obj: QFrame, start_location: QRect, end_location: QRect):
        """this method for do animation frame tools

        Arguments:
            obj {QFrame} -- [object must be do animation effect]
            start_location {QRect} -- [start location for anime]
            end_location {QRect} -- [end location for anime]
        """
        self.anim = QPropertyAnimation(obj, b"geometry")
        self.anim.setDuration(100)
        self.anim.setStartValue(start_location)
        self.anim.setEndValue(end_location)
        self.anim.start()

    def do_anim_concat_frame_tools(self, obj: QFrame, start_location: QRect, end_location: QRect):
        """this method for do animation frame concat to frame tools tools

        Arguments:
            obj {QFrame} -- [object must be do animation effect]
            start_location {QRect} -- [start location for anime]
            end_location {QRect} -- [end location for anime]
        """

        self.anim_2 = QPropertyAnimation(obj, b"geometry")
        self.anim_2.setDuration(100)
        self.anim_2.setStartValue(start_location)
        self.anim_2.setEndValue(end_location)
        self.anim_2.start()