"""
    - Created on May 19/2020 - hacktorco
    - All rights reserved for hacktor team
"""


class BoxStyles:

    frame_border_style_type1: tuple = ("frame_border_style", """
        #frame_border_style{
            background-color: rgb(218, 181, 111);
            border-radius:10px;
        }
    """)

    frame_border_style_type2: tuple = ("frame_border_style", """
            #frame_border_style{
                background-color: #BCBCBC;
                border-radius:10px;
            }
    """)

    box_style: tuple = ("box_style", """
        #box_style{
            background-color: rgb(35, 35, 35);
            border-radius:10px;
        }
    """)

    picture_style: tuple = ("picture_style", """
        #picture_style{
            background-color: rgba(0, 0, 0, 0);
            color: rgb(255, 255, 255);
            font:  14px Roboto Cn;
            border:0;
            border-radius:0;
        }
    """)

    lbl_title_style: tuple = ("lbl_title_style", """
        #lbl_title_style{
            background-color: rgba(0, 0, 0, 0);
            color: rgb(255, 255, 255);
            font: bold 10px "Source Sans Pro Semibold";
            border:0;
            border-radius:0;
        }
    """)
