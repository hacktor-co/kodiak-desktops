"""
    - Created on May 17/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QFrame,
    QLabel, QSizePolicy,
    QSpacerItem, QGridLayout
)
from PyQt5.QtCore import (Qt, QRect, QSize)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)

from commons.constants.app_paths import AppPaths
from .top_navigation_bar_containers_styles import TopNavigationBarContainersStyles


class TopNavigationBarContainers:
    
    def __init__(self):
        super(TopNavigationBarContainers, self).__init__()

    def setup_ui(self, containers: QFrame, main_gridLayout: QGridLayout):
        self.frame_location_box = QFrame(containers)
        self.frame_location_box.setFrameShape(QFrame.StyledPanel)
        self.frame_location_box.setFrameShadow(QFrame.Raised)
        self.frame_location_box.setObjectName("frame_location_box")
        
        self.vlayout_location_box = QVBoxLayout(self.frame_location_box)
        self.vlayout_location_box.setContentsMargins(0, 0, 71, 0)
        self.vlayout_location_box.setObjectName("vlayout_location_box")
        self.location_box = QLabel(self.frame_location_box)
        self.location_box.setText("DevOps")
        self.location_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.location_box.setObjectName(TopNavigationBarContainersStyles.location_box_style[0])
        self.location_box.setStyleSheet(TopNavigationBarContainersStyles.location_box_style[1])
        self.location_box.setAlignment(Qt.AlignCenter)
        self.location_box.setOpenExternalLinks(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_box.sizePolicy().hasHeightForWidth())
        self.location_box.setSizePolicy(sizePolicy)
        self.location_box.setMinimumSize(QSize(370, 33))
        self.location_box.setMaximumSize(QSize(370, 33))
        del sizePolicy
        self.vlayout_location_box.addWidget(self.location_box, 0, Qt.AlignHCenter)
        main_gridLayout.addWidget(self.frame_location_box, 0, 2, 1, 1)

        self.components_frame = QFrame(containers)
        self.components_frame.setMinimumSize(QSize(181, 51))
        self.components_frame.setMaximumSize(QSize(181, 51))
        self.components_frame.setFrameShape(QFrame.StyledPanel)
        self.components_frame.setFrameShadow(QFrame.Raised)
        self.components_frame.setObjectName("components_frame")

        self.item_user = QLabel(self.components_frame)
        self.item_user.setGeometry(QRect(0, 10, 34, 34))
        self.item_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_user.setAccessibleName(TopNavigationBarContainersStyles.item_notification_style[0])
        self.item_user.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_user.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/user_logo.svg"))
        self.item_user.setAlignment(Qt.AlignCenter)
        self.item_user.setObjectName("item_user")

        self.item_message = QLabel(self.components_frame)
        self.item_message.setObjectName("item_message")
        self.item_message.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_message.setGeometry(QRect(95, 10, 34, 34))
        self.item_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_message.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/message_logo.svg"))
        self.item_message.setAlignment(Qt.AlignCenter)

        self.item_notification = QLabel(self.components_frame)
        self.item_notification.setGeometry(QRect(47, 10, 34, 34))
        self.item_notification.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_notification.setAccessibleName(TopNavigationBarContainersStyles.item_notification_style[0])
        self.item_notification.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_notification.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notification_logo.svg"))
        self.item_notification.setAlignment(Qt.AlignCenter)
        self.item_notification.setObjectName("item_notification")

        self.item_search = QLabel(self.components_frame)
        self.item_search.setObjectName("item_search")
        self.item_search.setGeometry(QRect(142, 10, 34, 34))
        self.item_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_search.setAccessibleName(TopNavigationBarContainersStyles.item_notification_style[0])
        self.item_search.setStyleSheet(TopNavigationBarContainersStyles.item_notification_style[1])
        self.item_search.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/search_logo.svg"))
        self.item_search.setAlignment(Qt.AlignCenter)

        self.lbl_number_of_message = QLabel(self.components_frame)
        self.lbl_number_of_message.setGeometry(QRect(110, 5, 31, 26))
        self.lbl_number_of_message.setText("+25")
        self.lbl_number_of_message.setAlignment(Qt.AlignCenter)
        self.lbl_number_of_message.setObjectName(TopNavigationBarContainersStyles.notify_number_of_box_style[0])
        self.lbl_number_of_message.setStyleSheet(TopNavigationBarContainersStyles.notify_number_of_box_style[1])

        self.lbl_number_of_notification = QLabel(self.components_frame)
        self.lbl_number_of_notification.setGeometry(QRect(60, 5, 31, 26))
        self.lbl_number_of_notification.setText("+99")
        self.lbl_number_of_notification.setAlignment(Qt.AlignCenter)
        self.lbl_number_of_notification.setObjectName(TopNavigationBarContainersStyles.notify_number_of_box_style[0])
        self.lbl_number_of_notification.setStyleSheet(TopNavigationBarContainersStyles.notify_number_of_box_style[1])

        main_gridLayout.addWidget(self.components_frame, 0, 0, 1, 1)