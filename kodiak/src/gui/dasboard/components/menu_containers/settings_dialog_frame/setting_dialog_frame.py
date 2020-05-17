"""

"""

from PyQt5.QtWidgets import (QFrame, QLabel)
from PyQt5.QtCore import (Qt, QRect)
from PyQt5.QtGui import (QIcon, QPixmap, QCursor)

from commons.constants.app_paths import AppPaths
from .setting_dialog_frame_styles import SettingDialogFrameStyles


class SettingDialogFrame:

    def __init__(self):
        super(SettingDialogFrame, self).__init__()

    def setup_ui(self, containers: QFrame):

        self.frame_concat_to_frame_setting = QFrame(containers)
        self.frame_concat_to_frame_setting.setGeometry(QRect(1120, 280, 161, 78))
        self.frame_concat_to_frame_setting.setStyleSheet(SettingDialogFrameStyles.all_frame_style)
        self.frame_concat_to_frame_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_setting.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_setting.setObjectName("frame_concat_to_frame_setting")
        self.lbl_close_frame_setting = QLabel(self.frame_concat_to_frame_setting)
        self.lbl_close_frame_setting.setGeometry(QRect(5, 5, 21, 21))
        self.lbl_close_frame_setting.setCursor(QCursor(Qt.PointingHandCursor))

        self.lbl_close_frame_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        self.lbl_close_frame_setting.setObjectName("lbl_close_frame_setting")

        self.card_plugin = QLabel(self.frame_concat_to_frame_setting)
        self.card_plugin.setText("Add Plugin")
        self.card_plugin.setGeometry(QRect(40, 20, 71, 46))
        self.card_plugin.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_plugin.setStyleSheet(SettingDialogFrameStyles.cards_in_frame_style)
        self.card_plugin.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_plugin.setObjectName("card_plugin")

        self.pic_plugin_logo = QLabel(self.frame_concat_to_frame_setting)
        self.pic_plugin_logo.setGeometry(QRect(55, 5, 41, 31))
        self.pic_plugin_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_plugin_logo.setStyleSheet(SettingDialogFrameStyles.transparent_color_style)
        self.pic_plugin_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/plugin_icon.svg"))
        self.pic_plugin_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_plugin_logo.setObjectName("pic_plugin_logo")

        self.frame_setting = QFrame(containers)
        self.frame_setting.setGeometry(QRect(1240, 280, 91, 78))
        self.frame_setting.setStyleSheet(SettingDialogFrameStyles.all_frame_style)
        self.frame_setting.setObjectName("frame_setting")
        self.frame_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_setting.setFrameShadow(QFrame.Raised)

        self.lbl_setting = QLabel(self.frame_setting)
        self.lbl_setting.setText("Setting")
        self.lbl_setting.setGeometry(QRect(0, 27, 91, 21))
        self.lbl_setting.setStyleSheet(SettingDialogFrameStyles.lbl_frames_style)
        self.lbl_setting.setAlignment(Qt.AlignCenter)
        self.lbl_setting.setObjectName("lbl_setting")

        self.lbl_ellipse_setting = QLabel(self.frame_setting)
        self.lbl_ellipse_setting.setGeometry(QRect(0, 43, 91, 21))
        self.lbl_ellipse_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/ellipse_logo.svg"))
        self.lbl_ellipse_setting.setAlignment(Qt.AlignCenter)
        self.lbl_ellipse_setting.setObjectName("lbl_ellipse_setting")
        self.lbl_ellipse_setting.setStyleSheet(SettingDialogFrameStyles.transparent_color_style)
