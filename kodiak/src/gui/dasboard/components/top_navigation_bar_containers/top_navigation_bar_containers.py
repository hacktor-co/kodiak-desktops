"""
    - Created on May 17/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QFrame,
    QLabel
)
from PyQt5.QtCore import (Qt, QRect)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)

from commons.constants.app_paths import AppPaths
from .top_navigation_bar_containers_styles import TopNavigationBarContainersStyles


class TopNavigationBarContainers:
    
    def __init__(self):
        super(TopNavigationBarContainers, self).__init__()

    def setup_ui(self, containers: QFrame):

        self.item_user = QLabel(containers)
        self.item_user.setGeometry(QRect(23, 63, 34, 34))
        self.item_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_user.setAccessibleName(TopNavigationBarContainersStyles.item_notification_style[0])
        self.item_user.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_user.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/user_logo.svg"))
        self.item_user.setAlignment(Qt.AlignCenter)
        self.item_user.setObjectName("item_user")

        self.item_message = QLabel(containers)
        self.item_message.setObjectName("item_message")
        self.item_message.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_message.setGeometry(QRect(118, 63, 34, 34))
        self.item_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_message.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/message_logo.svg"))
        self.item_message.setAlignment(Qt.AlignCenter)

        self.item_notification = QLabel(containers)
        self.item_notification.setGeometry(QRect(70, 63, 34, 34))
        self.item_notification.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_notification.setAccessibleName(TopNavigationBarContainersStyles.item_notification_style[0])
        self.item_notification.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_notification.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notification_logo.svg"))
        self.item_notification.setAlignment(Qt.AlignCenter)
        self.item_notification.setObjectName("item_notification")

        self.item_search = QLabel(containers)
        self.item_search.setObjectName("item_search")
        self.item_search.setGeometry(QRect(175, 63, 34, 34))
        self.item_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_search.setAccessibleName(TopNavigationBarContainersStyles.item_notification_style[0])
        self.item_search.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_search.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/search_logo.svg"))
        self.item_search.setAlignment(Qt.AlignCenter)

        self.location_box = QLabel(containers)
        self.location_box.setText("DevOps")
        self.location_box.setGeometry(QRect(455, 63, 370, 33))
        self.location_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.location_box.setObjectName(TopNavigationBarContainersStyles.search_box_style[0])
        self.location_box.setStyleSheet(TopNavigationBarContainersStyles.search_box_style[1])
        self.location_box.setAlignment(Qt.AlignCenter)
        self.location_box.setOpenExternalLinks(False)

        self.icon_location_box = QLabel(containers)
        self.icon_location_box.setGeometry(QRect(455, 65, 31, 31))
        self.icon_location_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon_location_box.setObjectName("icon_location_box")
        self.icon_location_box.setStyleSheet(TopNavigationBarContainersStyles.transparent_color_style)
        self.icon_location_box.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/location_logo.svg"))
        self.icon_location_box.setAlignment(Qt.AlignCenter)
        self.icon_location_box.setOpenExternalLinks(False)

        self.notify_box_message = QLabel(containers)
        self.notify_box_message.setGeometry(QRect(136, 56, 34, 34))
        self.notify_box_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.notify_box_message.setObjectName(TopNavigationBarContainersStyles.notify_box_style[0])
        self.notify_box_message.setStyleSheet(TopNavigationBarContainersStyles.notify_box_style[1])
        self.notify_box_message.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notify_box.svg"))
        self.notify_box_message.setAlignment(Qt.AlignCenter)

        self.notify_box_notification = QLabel(containers)
        self.notify_box_notification.setGeometry(QRect(85, 56, 34, 34))
        self.notify_box_notification.setCursor(QCursor(Qt.PointingHandCursor))
        self.notify_box_notification.setObjectName(TopNavigationBarContainersStyles.notify_box_style[0])
        self.notify_box_notification.setStyleSheet(TopNavigationBarContainersStyles.notify_box_style[1])
        self.notify_box_notification.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notify_box.svg"))
        self.notify_box_notification.setAlignment(Qt.AlignCenter)

        self.lbl_number_of_message = QLabel(containers)
        self.lbl_number_of_message.setGeometry(QRect(140, 61, 31, 21))
        self.lbl_number_of_message.setText("+0")
        self.lbl_number_of_message.setObjectName(TopNavigationBarContainersStyles.notify_number_of_box_style[0])
        self.lbl_number_of_message.setStyleSheet(TopNavigationBarContainersStyles.notify_number_of_box_style[1])

        self.lbl_number_of_notification = QLabel(containers)
        self.lbl_number_of_notification.setText("+99")
        self.lbl_number_of_notification.setGeometry(QRect(90, 61, 31, 21))
        self.lbl_number_of_notification.setObjectName(TopNavigationBarContainersStyles.notify_number_of_box_style[0])
        self.lbl_number_of_notification.setStyleSheet(TopNavigationBarContainersStyles.notify_number_of_box_style[1])
