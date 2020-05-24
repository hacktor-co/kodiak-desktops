"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (QLabel, QFrame)
from PyQt5.QtGui import (QPixmap,QCursor)
from PyQt5.QtCore import (Qt,  QRect)

from .box_devops_part_styles import BoxDevopsPartStyles

class BoxDevopsPart:
    def __init__(self):
        super(BoxDevopsPart, self).__init__()

    def create_box(self, containers: QFrame, count_box: int, image: QPixmap = None, title:str = "Sy-Mon",box_type : bool=True, start_location: int = 30):

        """this method for create create_deatailes_box

        Arguments:
            containers {QFrame} -- [parent layout]
            count_box {int} -- [count for create]

        Keyword Arguments:
            title {str} -- [title in box] (default: {"DOCKER MONITORING"})
            image {str} -- [image in box] (default: {None})
            box_type {box type color type star box ...} -- [description] (default: {True})
            start_location {int} -- [ create box in location] (default: {30})

        Returns:
            [int] -- [location for use create other box]
        """
        for box in range(0,count_box):
            frame_border = QFrame(containers)

            if box != 0:
                frame_border.move(int(start_location)*box+138+20, 20)
                frame_border.resize(138, 138)
            else:
                frame_border.move(int(start_location), 20)
                frame_border.resize(138, 138)
            frame_border.setCursor(QCursor(Qt.PointingHandCursor))

            if box_type:
                frame_border.setObjectName(BoxDevopsPartStyles.frame_border_style_type1[0])
                frame_border.setStyleSheet(BoxDevopsPartStyles.frame_border_style_type1[1])
            else:
                frame_border.setObjectName(BoxDevopsPartStyles.frame_border_style_type2[0])
                frame_border.setStyleSheet(BoxDevopsPartStyles.frame_border_style_type2[1])
                
            frame_border.setFrameShape(QFrame.StyledPanel)
            frame_border.setFrameShadow(QFrame.Raised)
            
            devops_box = QFrame(frame_border)
            devops_box.setGeometry(QRect(3, 3, 133, 133))
            devops_box.setCursor(QCursor(Qt.PointingHandCursor))
            devops_box.setObjectName(BoxDevopsPartStyles.devops_box_style[0])
            devops_box.setStyleSheet(BoxDevopsPartStyles.devops_box_style[1])
            devops_box.setFrameShape(QFrame.StyledPanel)
            devops_box.setFrameShadow(QFrame.Raised)
            if image != None:
                pic_symon = QLabel(devops_box)
                pic_symon.setGeometry(QRect(0, 40, 131, 51))
                pic_symon.setObjectName(BoxDevopsPartStyles.pic_symon_style[0])
                pic_symon.setStyleSheet(BoxDevopsPartStyles.pic_symon_style[1])
                pic_symon.setPixmap(image)
                pic_symon.setAlignment(Qt.AlignCenter)
            if title != None:
                lbl_symon = QLabel(devops_box)
                lbl_symon.setGeometry(QRect(0, 100, 133, 20))
                lbl_symon.setObjectName(BoxDevopsPartStyles.lbl_symon_style[0])
                lbl_symon.setStyleSheet(BoxDevopsPartStyles.lbl_symon_style[1])
                lbl_symon.setAlignment(Qt.AlignCenter)
                lbl_symon.setText(title)

        return (int(start_location*(box+1))+138)+20