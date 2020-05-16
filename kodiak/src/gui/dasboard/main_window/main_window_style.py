# -*- coding: utf-8 -*-
"""
    - Created on May 16/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package is main window styles
"""


class DashboardMainWindowStyles:
    #---------------------------------------------
    #Enumurate Styles
    central_widget_style: str = """

        margin: 0;
        padding: 0;
    """

    lis_style: str = """

        padding:15px;
    """

    item_notification_style: str = """

        font: 75 9pt \"Roboto\";
    """

    notify_box_style: str = """

        font: 75 9pt \"Roboto\";
        background-color: rgba(255, 255, 255, 0);
    """

    notify_number_of_box_style: str = """

        color: rgb(255, 255, 255);
        font: bold  12px \"Caviar Dreams\";
        background-color: rgba(255, 255, 255, 0);
    """

    all_frame_style: str ="""

        background-color: rgb(219, 182, 111);
        border-radius:5px;
        color: rgb(55, 55, 55);
    """

    cards_in_frame_style: str = """

        background-color: rgb(232, 199, 137);
        border-radius:5px;
        padding-bottom:5px;
        font:  12px \"Roboto Lt\";
        color: rgb(55, 55, 55);
    """

    transparent_color_style:str = """

        background-color: rgba(255, 255, 255, 0);
    """

    lbl_frames_style:str = """

        font: bold 17px \"Roboto Cn\";
        color: rgb(0, 0, 0);
    """
    #---------------------------------------------

    main_page_style: str = ("main_page_style", """

        #main_page_style {
            font: 8pt "Roboto";
            background-color: rgb(22, 22, 21);
            color: rgb(255, 255, 255);
            margin: 0;
            padding: 0;
        }
    """)

    main_window_containers_style: str = ("main_window_containers_style", """

        #main_window_containers_style {
            margin:0;
            padding:0;
        }
    """)

    navigation_menu_style: str = ("navigation_menu_style", """

        #navigation_menu_style {
            background-color: rgb(38, 38, 38);
            color: rgb(255, 255, 255);
            font: 8pt \"Roboto\";
        }
    """
    )

    lbl_time_style: str = ("lbl_time_style", """

        #lbl_time_style {
                color: rgb(255, 255, 255);
                font: bold  14px \"Caviar Dreams\";
            }
    """
    )

    lbl_date_style: str = ("lbl_date_style", """

        #lbl_date_style {
                color: rgb(255, 255, 255);
                font: bold  9px \"Caviar Dreams\";
            }
    """
    )

    search_box_style: str = ("search_box_style", """
        #search_box_style {
            font: bold 14px \"LEMON MILK\";
            background-color: rgb(59, 59, 59);
            color: rgb(255, 255, 255);
            border-radius:15px;
        }
        """
    )
