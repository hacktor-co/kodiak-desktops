"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout,QHBoxLayout,
    QLabel, QFrame
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
from .star_box_style import StarBoxStyles


class StarBox:
    def __init__(self):
        super(StarBox, self).__init__()

    def create_star(self, card_containers: QFrame, count_star_type1 : int, count_star_type2: int, star_type:bool=True):
        """this method create star rate box 

        Arguments:
            card_containers {QFrame} -- [this argument parent layout]
            count_star_type1 {int} -- [this argument count star yellow in box]
            count_star_type2 {int} -- [this argument count star yellow in box]
        """
        self.frame_star_group = QFrame(card_containers)
        self.frame_star_group.setGeometry(QRect(25, 105, 91, 24))

        self.frame_star_group.setObjectName(StarBoxStyles.frame_star_group_style[0])
        self.frame_star_group.setStyleSheet(StarBoxStyles.frame_star_group_style[1])
        
        self.hl_frame_star_group = QHBoxLayout(self.frame_star_group)
        self.hl_frame_star_group.setContentsMargins(0, 0, 0, 0)
        self.hl_frame_star_group.setSpacing(0)
        self.hl_frame_star_group.setObjectName("hl_frame_star_group")

        path_star_type_1 : str = [
            AppPaths.GUI_ASSETS_ICONS_PATH + 
            "/main_window/star-yellow-logo.svg" 
            if star_type else AppPaths.GUI_ASSETS_ICONS_PATH + 
            "/main_window/star-white-logo.svg"
            ][0]

        path_star_type_2 : str = [
            AppPaths.GUI_ASSETS_ICONS_PATH +
            "/main_window/star-gray.svg" 
            if star_type else 
            AppPaths.GUI_ASSETS_ICONS_PATH +
            "/main_window/star-gray-yellow.svg"
            ][0]

        for yellow_star in range(count_star_type1):
            
            self.pic_star_type1 = QLabel(self.frame_star_group)
            self.pic_star_type1.setObjectName(StarBoxStyles.stars_style[0])
            self.pic_star_type1.setStyleSheet(StarBoxStyles.stars_style[1])
            self.pic_star_type1.setPixmap(QPixmap(path_star_type_1))
            self.hl_frame_star_group.addWidget(self.pic_star_type1)

        for gray_star in range(count_star_type2):
            
            self.pic_star_type2 = QLabel(self.frame_star_group)
            self.pic_star_type2.setObjectName(StarBoxStyles.stars_style[0])
            self.pic_star_type2.setStyleSheet(StarBoxStyles.stars_style[1])
            self.pic_star_type2.setPixmap(QPixmap(path_star_type_2))
            self.hl_frame_star_group.addWidget(self.pic_star_type2)
            