"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (QLabel, QFrame)
from PyQt5.QtGui import QCursor

from PyQt5.QtCore import (Qt,QRect)

from .box_styles import BoxStyles
class Box:
    
    def __init__(self):
        super(Box, self).__init__()
    
    def create_box(self, containers: QFrame, count_box: int, title:str = "" ,box_type : bool = True, start_location: int = 30, count_star_type1: int = 3, count_star_type2:int = 2):
        """this method for create box mode2

        Arguments:
            containers {QFrame} -- [parent layout]
            count_box {int} -- [count for create]

        Keyword Arguments:
            title {str} -- [title in box] (default: {""})
            box_type {box type color type star box ...} -- [description] (default: {True})
            start_location {int} -- [ create box in location] (default: {30})

        Returns:
            [int] -- [location for use create other box]
        """
        from ..star_box.starbox import StarBox
        for box_enumerate in range(count_box):

            card_details = QFrame(containers)
            if box_enumerate != 0:
                card_details.move(int(start_location)*box_enumerate+138+20, 20)
                card_details.resize(138, 138)
            else:
                card_details.move(int(start_location), 20)
                card_details.resize(138, 138)

            card_details.setCursor(QCursor(Qt.PointingHandCursor))
            
            if box_type:
                StarBox().create_star( card_containers= card_details, count_star_type1 = count_star_type1, count_star_type2 = count_star_type2)
                card_details.setObjectName(BoxStyles.card_details_style_type_1[0])
                card_details.setStyleSheet(BoxStyles.card_details_style_type_1[1])
            else:
                StarBox().create_star( card_containers= card_details, count_star_type1 = count_star_type1, count_star_type2 = count_star_type2, star_type = False)
                card_details.setObjectName(BoxStyles.card_details_style_type_2[0])
                card_details.setStyleSheet(BoxStyles.card_details_style_type_2[1])

            lbl_title = QLabel(card_details)
            lbl_title.setGeometry(QRect(0, 10, 138, 20))
            lbl_title.setObjectName(BoxStyles.lbl_title_styles[0])
            lbl_title.setStyleSheet(BoxStyles.lbl_title_styles[1])
            lbl_title.setAlignment(Qt.AlignCenter)
            lbl_title.setText(title)
            card_details.setFrameShape(QFrame.StyledPanel)
            card_details.setFrameShadow(QFrame.Raised)
    
        return (int(start_location*(box_enumerate+1))+138)+20
      
