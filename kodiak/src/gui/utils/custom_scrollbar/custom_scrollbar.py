"""
    -(Factory Design Pattern )
    - Created on May June 6/10/2020 - hacktorco
    - All rights reserved for hacktor team
"""


class ScrollBar:
    def __init__(self):
        super(ScrollBar, self).__init__()

    @staticmethod
    def create_scrollbar(orientation: str = "both"):
        """
        this method create scroll bar  -- > > this is a Factory Method
        Arguments:
            [str] - orientation default : both = vertical & Horizontal scrollbar
        Returns:
            [class]
        """
        if orientation == "both":
            return BothScrollBar.create()
        elif orientation == "vertical":
            return VerticalScrollBar.create()
        elif orientation == "horizontal":
            return  HorizontalScrollBar.create()


class BothScrollBar:
    def __init__(self):
        super(BothScrollBar, self).__init__()

    @staticmethod
    def create():
        """
        this method create both scroll bar
        """
        __both_scroll_bar__: str = """        
            QScrollBar:vertical
             {
                 background-color:#3B3B3B;
                 width: 15px;
                 margin: 15px 3px 15px 3px;
                 border: 1px transparent #2A2929;
                 border-radius: 4px;
             }
            
             QScrollBar::handle:vertical
             {
                 background-color: #646464;         /* #605F5F; */
                 min-height: 5px;
                 border-radius: 4px;
             }
            
             QScrollBar::sub-line:vertical
             {
                 margin: 3px 0px 3px 0px;
                 border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: top;
                 subcontrol-origin: margin;
             }
            
             QScrollBar::add-line:vertical
             {
                 margin: 3px 0px 3px 0px;
                 border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: bottom;
                 subcontrol-origin: margin;
             }
            
             QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
             {
            
                 border-image: url(:/qss_icons/rc/up_arrow.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: top;
                 subcontrol-origin: margin;
             }
            
            
             QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
             {
                 border-image: url(:/qss_icons/rc/down_arrow.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: bottom;
                 subcontrol-origin: margin;
             }
            
             QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
             {
                 background: none;
             }
            
            
             QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
             {
                 background: none;
             }
             
             QScrollBar:horizontal
                 {
                     height: 15px;
                     margin: 3px 15px 3px 15px;
                     border: 1px transparent #2A2929;
                     border-radius: 4px;
                     background-color: #3B3B3B;    /* #2A2929; */
                 }
                
                 QScrollBar::handle:horizontal
                 {
                     background-color: #646464;      /* #605F5F; */
                     min-width: 5px;
                     border-radius: 4px;
                 }
                
                 QScrollBar::add-line:horizontal
                 {
                     margin: 0px 3px 0px 3px;
                     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
                     width: 10px;
                     height: 10px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                 }
                
                 QScrollBar::sub-line:horizontal
                 {
                     margin: 0px 3px 0px 3px;
                     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
                     height: 10px;
                     width: 10px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                 }
                
                 QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
                 {
                     border-image: url(:/qss_icons/rc/right_arrow.png);
                     height: 10px;
                     width: 10px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                 }
                
                
                 QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
                 {
                     border-image: url(:/qss_icons/rc/left_arrow.png);
                     height: 10px;
                     width: 10px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                 }
                
                 QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
                 {
                     background: none;
                 }
                
                 QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                 {
                     background: none;
                 }
        """
        return __both_scroll_bar__


class VerticalScrollBar:
    def __init__(self):
        super(VerticalScrollBar, self).__init__()

    @staticmethod
    def create():
        """
        this method create vertical scroll bar
        """
        __vertical_scroll_bar__: str = """        
            QScrollBar:vertical
             {
                 background-color:#3B3B3B;
                 width: 15px;
                 margin: 15px 3px 15px 3px;
                 border: 1px transparent #2A2929;
                 border-radius: 4px;
             }

             QScrollBar::handle:vertical
             {
                 background-color: #646464;         /* #605F5F; */
                 min-height: 5px;
                 border-radius: 4px;
             }

             QScrollBar::sub-line:vertical
             {
                 margin: 3px 0px 3px 0px;
                 border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: top;
                 subcontrol-origin: margin;
             }

             QScrollBar::add-line:vertical
             {
                 margin: 3px 0px 3px 0px;
                 border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: bottom;
                 subcontrol-origin: margin;
             }

             QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
             {

                 border-image: url(:/qss_icons/rc/up_arrow.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: top;
                 subcontrol-origin: margin;
             }


             QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
             {
                 border-image: url(:/qss_icons/rc/down_arrow.png);
                 height: 10px;
                 width: 10px;
                 subcontrol-position: bottom;
                 subcontrol-origin: margin;
             }

             QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
             {
                 background: none;
             }


             QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
             {
                 background: none;
             }
        """
        return __vertical_scroll_bar__


class HorizontalScrollBar:
    def __init__(self):
        super(HorizontalScrollBar, self).__init__()

    @staticmethod
    def create():
        """
        this method create Horizontal scroll bar
        """
        __horizontal_scroll_bar__: str = """        
                QScrollBar:horizontal
                 {
                     height: 15px;
                     margin: 3px 15px 3px 15px;
                     border: 1px transparent #2A2929;
                     border-radius: 4px;
                     background-color: #3B3B3B;    /* #2A2929; */
                 }
                
                 QScrollBar::handle:horizontal
                 {
                     background-color: #646464;      /* #605F5F; */
                     min-width: 5px;
                     border-radius: 4px;
                 }
                
                 QScrollBar::add-line:horizontal
                 {
                     margin: 0px 3px 0px 3px;
                     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
                     width: 10px;
                     height: 10px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                 }
                
                 QScrollBar::sub-line:horizontal
                 {
                     margin: 0px 3px 0px 3px;
                     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
                     height: 10px;
                     width: 10px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                 }
                
                 QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
                 {
                     border-image: url(:/qss_icons/rc/right_arrow.png);
                     height: 10px;
                     width: 10px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                 }
                
                
                 QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
                 {
                     border-image: url(:/qss_icons/rc/left_arrow.png);
                     height: 10px;
                     width: 10px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                 }
                
                 QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
                 {
                     background: none;
                 }
                
                 QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                 {
                     background: none;
                 }

        """
        return __horizontal_scroll_bar__
