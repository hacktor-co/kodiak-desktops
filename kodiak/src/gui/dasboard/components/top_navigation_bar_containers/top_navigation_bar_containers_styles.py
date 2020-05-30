# -*- coding: utf-8 -*-
"""
    - Created on May 17/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from commons.constants.app_paths import AppPaths


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
            border-radius:12px;
            background-color: rgb(255, 58,71);
        }
    """)

    item_notification_style: tuple = ("item_notification_style", """
        [accessibleName="item_notification_style"] {
            font: 75 9pt "Roboto";
        }
    """)

    location_box_style: tuple = ("location_box_style", """
        #location_box_style {
            font: bold 14px "LEMON MILK";
            background-color: rgb(59, 59, 59);
            color: rgb(255, 255, 255);
            border-radius:15px;
            background-image: url("""+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/location_logo.svg").replace("\\","/")+""");
            background-repeat: no-repeat;
            background-position: left center;
            background-origin: content;
            padding-left:10px;
        }
    """)
