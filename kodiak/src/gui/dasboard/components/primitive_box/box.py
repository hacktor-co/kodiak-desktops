"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
        QLabel, QFrame, 
        QVBoxLayout, QGridLayout, 
        QSpacerItem, QSizePolicy
    )
from PyQt5.QtGui import (QPixmap,QCursor)
from PyQt5.QtCore import (Qt,  QRect)

from .box_styles import BoxStyles

class Box:
    def __init__(self):
        super(Box, self).__init__()

    def create_box(self, containers: QFrame, count_box: int, frame_gridLayout:QGridLayout, start_index:int=0, image: QPixmap = None, title:str = "", box_type : bool = True):
        """this method for create primitive box

        Arguments:
            containers {QFrame} -- [parent layout]
            count_box {int} -- [count for create]

        Keyword Arguments:
            title {str} -- [title in box] (default: {""})
            image {str} -- [image in box] (default: {None})
            box_type {box type color type star box ...} -- [description] (default: {True})
            start_location {int} -- [ create box in location] (default: {30})
        """

        box_enumerate=0
        for box_enumerate in range(0,count_box):
            frame_border = QFrame(containers)
            frame_border.setCursor(QCursor(Qt.PointingHandCursor))
            frame_border.setMaximumSize(138,138)
            frame_border.setMinimumSize(138,138)
            if box_type:
                frame_border.setObjectName(BoxStyles.frame_border_style_type1[0])
                frame_border.setStyleSheet(BoxStyles.frame_border_style_type1[1])
            else:
                frame_border.setObjectName(BoxStyles.frame_border_style_type2[0])
                frame_border.setStyleSheet(BoxStyles.frame_border_style_type2[1])
                
            frame_border.setFrameShape(QFrame.StyledPanel)
            frame_border.setFrameShadow(QFrame.Raised)

            frame_border_vlayout = QVBoxLayout(frame_border)
            frame_border_vlayout.setContentsMargins(3, 3, 3, 3)
            frame_border_vlayout.setObjectName("frame_border_vlayout")
            
            box = QFrame(frame_border)
            box.setGeometry(QRect(3, 3, 133, 133))
            box.setCursor(QCursor(Qt.PointingHandCursor))
            box.setObjectName(BoxStyles.box_style[0])
            box.setStyleSheet(BoxStyles.box_style[1])
            box.setFrameShape(QFrame.StyledPanel)
            box.setFrameShadow(QFrame.Raised)

            box_vlayout = QVBoxLayout(box)
            box_vlayout.setContentsMargins(-1, 40, -1, -1)
            box_vlayout.setObjectName("box_vlayout")

            if image != None:
                picture = QLabel(box)
                picture.setGeometry(QRect(0, 40, 131, 51))
                picture.setObjectName(BoxStyles.picture_style[0])
                picture.setStyleSheet(BoxStyles.picture_style[1])
                picture.setPixmap(image)
                picture.setAlignment(Qt.AlignCenter)
            if title != None:
                lbl_title = QLabel(box)
                lbl_title.setGeometry(QRect(0, 100, 133, 20))
                lbl_title.setObjectName(BoxStyles.lbl_title_style[0])
                lbl_title.setStyleSheet(BoxStyles.lbl_title_style[1])
                lbl_title.setAlignment(Qt.AlignCenter)
                lbl_title.setText(title)
            
            frame_gridLayout.addWidget(frame_border, 0, (box_enumerate + start_index), Qt.AlignLeft)
            
        return int(box_enumerate+1)