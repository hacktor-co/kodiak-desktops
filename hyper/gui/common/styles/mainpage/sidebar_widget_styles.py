#!/usr/bin/python3
"""
    - Created on jul 15/2019 - hacktorco
    - All rights reserved for hacktor team

    - all style sheet value of sidebar of main window
"""

main_widget_style = ("main_widget_style", """
    [accessibleName="main_window_style"] {
        background-color: #1F1F1F;
        min-width: 170px;
        max-width: 170px;
        min-height: 790px;
        max-height: 790px;
        border-left: 2px solid #10A1D7;
        padding: 0;
    }
""")

icon_holder_frame_style = ("icon_holder_frame_style", """
    [accessibleName="icon_holder_frame_style"] {
        background-color: #272E39;
        max-height: 150px;
        min-height: 150px;
        min-width: 170px;
        max-width: 170px;
        border-left: 2px solid #1197CA;
    }
""")

selected_button = ("selected_button", """
    [accessibleName="selected_button"] {
        background-color: #1F1F1F;
        max-height: 130px;
        min-height: 130px;
        min-width: 170px;
        max-width: 170px;
        border: 2px solid transparent;
        border-bottom: 2px solid #1197CA;
        border-top: 2px solid #1197CA;
    }
""")

not_selected_button = ("not_selected_button", """
    [accessibleName="not_selected_button"] {
        background-color: #272E39;
        max-height: 130px;
        min-height: 130px;
        min-width: 170px;
        max-width: 170px;
        border: 2px solid transparent;
        border-left: 2px solid #1197CA;
    }
""")
