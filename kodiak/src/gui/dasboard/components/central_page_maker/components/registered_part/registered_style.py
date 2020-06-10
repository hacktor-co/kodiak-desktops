"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from ......utils.custom_scrollbar.custom_scrollbar import ScrollBar


class RegisteredStyles:

    lbl_registered_style: tuple = ("lbl_registered_style", """
           #lbl_registered_style {
               font: bold 14px "LEMON MILK";
               color: rgb(255,255,255);
               background-color: rgb(0,213,126);
               border-radius: 5px;
           }
       """)

    frame_border_add_plugins_to_registered_style: tuple = ("frame_border_add_plugins_to_registered_style", """
    #frame_border_add_plugins_to_registered_style{
            background-color: #484848;
            border-radius:10px;
            }
        """
                                                           )
    card_add_plugins_to_registered_style: tuple = ("card_add_plugins_to_registered_style", """
    #card_add_plugins_to_registered_style{

            background-color: rgb(35, 35, 35);
            border-radius:10px;
        }

    """
                                                   )

    pic_add_plugin_to_registered_style: tuple = ("pic_add_plugin_to_registered_style", """

    #pic_add_plugin_to_registered_style{

        background-color: rgba(0, 0, 0, 0);
        color: rgb(255, 255, 255);
        font:  14px Roboto Cn;
        border:0;
        border-radius:0;

        }

    """
                                                 )

    registered_frame_style: tuple = ("registered_frame_style", """
    #registered_frame_style
    {
        background-color: rgb(34,34,34);
        border-radius:5px;
    }
    """+ScrollBar.create_scrollbar("both")
                                     )
    scroll_area_style: tuple = ("scroll_area_style", """
    #scroll_area_style
    {
        background-color: rgb(34,34,34);
    }
    """
                                )
