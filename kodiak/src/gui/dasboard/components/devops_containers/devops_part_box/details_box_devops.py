"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (QLabel, QFrame)
from PyQt5.QtGui import QCursor

from PyQt5.QtCore import (Qt,QRect)

from .details_box_devops_styles import DetailsBoxStylesDevops
class DetailsBoxDevops:
    
    def __init__(self):
        super(DetailsBoxDevops, self).__init__()
    
    def create_deatailes_box(self, containers: QFrame, count_box: int, title:str = "DOCKER MONITORING" ,box_type : bool=True, start_location: int = 30):
        """this method for create create_deatailes_box

        Arguments:
            containers {QFrame} -- [parent layout]
            count_box {int} -- [count for create]

        Keyword Arguments:
            title {str} -- [title in box] (default: {"DOCKER MONITORING"})
            box_type {box type color type star box ...} -- [description] (default: {True})
            start_location {int} -- [ create box in location] (default: {30})

        Returns:
            [int] -- [location for use create other box]
        """
        from ....components.star_box.starbox import StarBox
        for box in range(count_box):

            card_details = QFrame(containers)
            if box != 0:
                card_details.move(int(start_location)*box+138+20, 20)
                card_details.resize(138, 138)
            else:
                card_details.move(int(start_location), 20)
                card_details.resize(138, 138)

            card_details.setCursor(QCursor(Qt.PointingHandCursor))
            
            if box_type:
                StarBox().create_star( card_containers= card_details, count_star_type1 = 3, count_star_type2 = 2)
                card_details.setObjectName(DetailsBoxStylesDevops.card_details_style_type_1[0])
                card_details.setStyleSheet(DetailsBoxStylesDevops.card_details_style_type_1[1])
            else:
                StarBox().create_star( card_containers= card_details, count_star_type1 = 3, count_star_type2 = 2, star_type = False)
                card_details.setObjectName(DetailsBoxStylesDevops.card_details_style_type_2[0])
                card_details.setStyleSheet(DetailsBoxStylesDevops.card_details_style_type_2[1])

            lbl_title = QLabel(card_details)
            lbl_title.setGeometry(QRect(0, 10, 138, 20))
            lbl_title.setObjectName(DetailsBoxStylesDevops.lbl_title_styles[0])
            lbl_title.setStyleSheet(DetailsBoxStylesDevops.lbl_title_styles[1])
            lbl_title.setAlignment(Qt.AlignCenter)
            lbl_title.setText(title)
            card_details.setFrameShape(QFrame.StyledPanel)
            card_details.setFrameShadow(QFrame.Raised)
    
        return (int(start_location*(box+1))+138)+20
      
