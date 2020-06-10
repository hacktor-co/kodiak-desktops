"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from ....utils.custom_scrollbar.custom_scrollbar import ScrollBar

class CentralPageMakerStyle:

    lbl_title_style: tuple = ("lbl_title_style", """
        #lbl_title_style {
            color: rgb(255, 255, 255);
            font: 14px "LEMON MILK";
        }
    """)

    scroll_area_page_containers_style: tuple = ("scroll_area_page_containers_style", """
        #scroll_area_page_containers_style{
                background-color: rgb(22, 22, 21);
        }
    """+ScrollBar().create_scrollbar("both")
                                                )
