"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from commons.constants.app_paths import AppPaths

class ToolBarStyles:

    main_page_maximaize_style: str = """
    #main_page_style {
            font: 8pt "Roboto";
            background-color: rgb(22, 22, 21);
            color: rgb(255, 255, 255);
            margin: 0;
            padding: 0;
            border: none;
        }
    """

    
    navigation_maximaize_menu: str = """
            #navigation_menu_style {
            background-color: rgb(38, 38, 38);
            color: rgb(255, 255, 255);
            font: 8pt "Roboto";
        }
    """

    toolbar_maximaize_style: str = """
        #toolbar_style {
            background-color: rgb(38, 38, 38);
            color: rgb(255, 255, 255);
            font: 8pt "Roboto";
        }
    """

    main_page_minimaize_style: str = """
    #main_page_style {
            border-radius: 20px;
            font: 8pt "Roboto";
            background-color: rgb(22, 22, 21);
            color: rgb(255, 255, 255);
            margin: 0;
            padding: 0;
            border: none;
        }
    """

    
    navigation_minimaize_menu: str = """
       #navigation_menu_style {
            border-bottom-right-radius: 20px;
            background-color: rgb(38, 38, 38);
            color: rgb(255, 255, 255);
            font: 8pt "Roboto";
        }
    """

    toolbar_minimize_style: tuple = ("toolbar_style", """
    #toolbar_style {
            background-color: rgb(38, 38, 38);
            border-top-left-radius:20px;
            border-top-right-radius:20px;
            color: rgb(255, 255, 255);
            font: 8pt "Roboto";
        }
    """)

    btn_close_style: tuple = ("btn_close_style",

        "#btn_close_style {"
        "background-color: rgba(0, 0, 0, 0);"
        " image: url("+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo_main.svg").replace("\\","/")+");"
        "}"

        "#btn_close_style:hover {"
        "background-color: rgba(0, 0, 0, 0);"
        " image: url("+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo_main_hover.svg").replace("\\","/")+");"
        "}"
        
    )
    
    
    btn_maximize_style: tuple = ("btn_maximize_style",
        "#btn_maximize_style {"
        "background-color: rgba(0, 0, 0, 0);"
        " image: url("+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/maximize_logo_main.svg").replace("\\","/")+");"
        "}"

        "#btn_maximize_style:hover {"
        "background-color: rgba(0, 0, 0, 0);"
        " image: url("+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/maximize_logo_main_hover.svg").replace("\\","/")+");"
        "}"
        
    )

    btn_minimize_style: tuple = ("btn_minimize_style",
        "#btn_minimize_style {"
        "background-color: rgba(0, 0, 0, 0);"
        " image: url("+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/minimize_logo_main.svg").replace("\\","/")+");"
        "}"

        "#btn_minimize_style:hover {"
        "background-color: rgba(0, 0, 0, 0);"
        " image: url("+(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/minimize_logo_main_hover.svg").replace("\\","/")+");"
        "}"
        
    )
