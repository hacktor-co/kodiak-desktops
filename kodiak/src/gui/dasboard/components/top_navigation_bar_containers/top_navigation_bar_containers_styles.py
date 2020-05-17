# -*- coding: utf-8 -*-
"""
    - Created on May 17/2020 - hacktorco
    - All rights reserved for hacktor team
"""


class TopNavigationBarContainersStyles:

    transparent_color_style: str = """
        background-color: rgba(255, 255, 255, 0);
    """

    notify_box_style: tuple = ("notify_box_style", """
        #notify_box_style {
            font: 75 9pt "Roboto";
            background-color: rgba(255, 255, 255, 0);
        }
    """)

    notify_number_of_box_style: tuple = ("notify_number_of_box_style", """
        #notify_number_of_box_style {
            color: rgb(255, 255, 255);
            font: bold  12px "Caviar Dreams";
            background-color: rgba(255, 255, 255, 0);
        }
    """)

    item_notification_style: tuple = ("item_notification_style", """
        [accessibleName="item_notification_style"] {
            font: 75 9pt "Roboto";
        }
    """)

    search_box_style: tuple = ("search_box_style", """
        #search_box_style {
            font: bold 14px "LEMON MILK";
            background-color: rgb(59, 59, 59);
            color: rgb(255, 255, 255);
            border-radius:15px;
        }
    """)
