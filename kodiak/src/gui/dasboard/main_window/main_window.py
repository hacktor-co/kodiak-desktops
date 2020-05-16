# -*- coding: utf-8 -*-
"""
    - Created on May 15/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create main window of application as dashboard

    - [mjghasempour, abolfazl]
"""

from PyQt5.QtWidgets import ( 
    QMainWindow, QWidget,
    QVBoxLayout, QFrame,
    QLabel
)

from PyQt5.QtCore import (
    Qt, QSize,
    QRect,QCoreApplication
)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)

from commons.constants.app_paths import AppPaths
from .main_window_style import DashboardMainWindowStyles


class DashboardMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(DashboardMainWindow, self).__init__(parent)
        self.__setup_ui__()

    def __setup_ui__(self):
        
        self.setObjectName(DashboardMainWindowStyles.main_page_style[0])
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(1346, 928)
        self.setMinimumSize(QSize(1346, 928))
        self.setMaximumSize(QSize(1346, 928))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAcceptDrops(False)
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        #Add Vertical Layout 
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #Add 
        self.containers = QFrame(self.centralwidget)
        self.containers.setObjectName(DashboardMainWindowStyles.main_window_containers_style[0])
        self.containers.setStyleSheet(DashboardMainWindowStyles.main_window_containers_style[1])
        self.containers.setFrameShape(QFrame.NoFrame)
        self.containers.setFrameShadow(QFrame.Plain)
        self.containers.setLineWidth(0)
        #Add Navigation
        self.navigation_menu = QFrame(self.containers)
        self.navigation_menu.setObjectName(DashboardMainWindowStyles.navigation_menu_style[0])
        self.navigation_menu.setStyleSheet(DashboardMainWindowStyles.navigation_menu_style[1])
        self.navigation_menu.setGeometry(QRect(1275, -10, 71, 948))
        self.navigation_menu.setFrameShape(QFrame.StyledPanel)
        self.navigation_menu.setFrameShadow(QFrame.Raised)
        #Add pic_main_logo
        self.pic_main_logo = QLabel(self.navigation_menu)
        self.pic_main_logo.setGeometry(QRect(13, 40, 44, 71))
    
        self.pic_main_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/kodiak_icon.svg"))
        self.pic_main_logo.setObjectName("pic_main_logo")
        #Add LblTime
        self.lbl_time = QLabel(self.navigation_menu)
        self.lbl_time.setGeometry(QRect(0, 120, 69, 20))
        self.lbl_time.setObjectName(DashboardMainWindowStyles.lbl_time_style[0])
        self.lbl_time.setStyleSheet(DashboardMainWindowStyles.lbl_time_style[1])
        self.lbl_time.setAlignment(Qt.AlignCenter)
        #Add lblDate
        self.lbl_date = QLabel(self.navigation_menu)
        self.lbl_date.setGeometry(QRect(0, 140, 71, 21))
        self.lbl_date.setObjectName(DashboardMainWindowStyles.lbl_date_style[0])
        self.lbl_date.setStyleSheet(DashboardMainWindowStyles.lbl_date_style[1])
        self.lbl_date.setAlignment(Qt.AlignCenter)

        self.verticalLayoutWidget = QWidget(self.navigation_menu)
        self.verticalLayoutWidget.setGeometry(QRect(0, 290, 64, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        #----------------------setup-li-----------------------------------------

        self.verticalLayoutWidget.setGeometry(QRect(0, 290, 64, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.containers_menu_li = QVBoxLayout(self.verticalLayoutWidget)
        self.containers_menu_li.setContentsMargins(0, 0, 0, 0)
        self.containers_menu_li.setSpacing(23)
        self.containers_menu_li.setObjectName("containers_menu_li")
        self.li_setting = QLabel(self.verticalLayoutWidget)
        self.li_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_setting.setStyleSheet(DashboardMainWindowStyles.lis_style)
        self.li_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/setting_logo.svg"))
        self.li_setting.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.li_setting.setObjectName("li_setting")
        self.containers_menu_li.addWidget(self.li_setting)
        self.li_menu = QLabel(self.verticalLayoutWidget)
        self.li_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_menu.setStyleSheet(DashboardMainWindowStyles.lis_style)
        self.li_menu.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/menu_logo.svg"))
        self.li_menu.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.li_menu.setObjectName("li_menu")
        self.containers_menu_li.addWidget(self.li_menu)
        self.li_chart = QLabel(self.verticalLayoutWidget)
        self.li_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_chart.setStyleSheet(DashboardMainWindowStyles.lis_style)
        self.li_chart.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/chart_logo.svg"))
        self.li_chart.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.li_chart.setObjectName("li_chart")
        self.containers_menu_li.addWidget(self.li_chart)
        self.li_box = QLabel(self.verticalLayoutWidget)
        self.li_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_box.setStyleSheet(DashboardMainWindowStyles.lis_style)
        self.li_box.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/box_logo.svg"))
        self.li_box.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.li_box.setObjectName("li_box")
        self.containers_menu_li.addWidget(self.li_box)
        self.li_brain = QLabel(self.verticalLayoutWidget)
        self.li_brain.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_brain.setStyleSheet(DashboardMainWindowStyles.lis_style)
        self.li_brain.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/brain_logo.svg"))
        self.li_brain.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.li_brain.setObjectName("li_brain")
        self.containers_menu_li.addWidget(self.li_brain)
        #-------------------------------end li-----------------------------------------------------

        #-----------------------------------setup_items--------------------------------------------
        self.item_user =QLabel(self.containers)
        self.item_user.setGeometry(QRect(23, 22, 34, 34))
        self.item_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_user.setStyleSheet(DashboardMainWindowStyles.item_notification_style)
        
        self.item_user.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/user_logo.svg"))
        self.item_user.setAlignment(Qt.AlignCenter)
        self.item_user.setObjectName("item_user")
        self.item_message = QLabel(self.containers)
        self.item_message.setGeometry(QRect(118, 22, 34, 34))
        self.item_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_message.setStyleSheet(DashboardMainWindowStyles.item_notification_style)
        
        self.item_message.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/message_logo.svg"))
        self.item_message.setAlignment(Qt.AlignCenter)
        self.item_message.setObjectName("item_message")
        self.item_notification = QLabel(self.containers)
        self.item_notification.setGeometry(QRect(70, 22, 34, 34))
        self.item_notification.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_notification.setStyleSheet(DashboardMainWindowStyles.item_notification_style)
        
        self.item_notification.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notification_logo.svg"))
        self.item_notification.setAlignment(Qt.AlignCenter)
        self.item_notification.setObjectName("item_notification")
        self.item_search = QLabel(self.containers)
        self.item_search.setGeometry(QRect(175, 22, 34, 34))
        self.item_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.item_search.setStyleSheet(DashboardMainWindowStyles.item_notification_style)
        
        self.item_search.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/search_logo.svg"))
        self.item_search.setAlignment(Qt.AlignCenter)
        self.item_search.setObjectName("item_search")
        #----------------------------------------------end_items------------------------------------------
        #-------------------------------------------------setup-location-box-----------------------------
        self.location_box =  QLabel(self.containers)
        self.location_box.setGeometry(QRect(488, 22, 370, 33))
        self.location_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.location_box.setObjectName(DashboardMainWindowStyles.search_box_style[0])
        self.location_box.setStyleSheet(DashboardMainWindowStyles.search_box_style[1])
        self.location_box.setAlignment(Qt.AlignCenter)
        self.location_box.setOpenExternalLinks(False)
        #icon in location box
        self.icon_location_box = QLabel(self.containers)
        self.icon_location_box.setGeometry(QRect(490, 25, 31, 31))
        self.icon_location_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon_location_box.setObjectName("icon_location_box")
        self.icon_location_box.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)    
        self.icon_location_box.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/location_logo.svg"))
        self.icon_location_box.setAlignment(Qt.AlignCenter)
        self.icon_location_box.setOpenExternalLinks(False)
        
        #----------------------------------------------end_location_box------------------------------------------
        #----------------------------------------------setup_notify_message--------------------------------------
        self.notify_box_message = QLabel(self.containers)
        self.notify_box_message.setGeometry(QRect(136, 15, 34, 34))
        self.notify_box_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.notify_box_message.setObjectName("notify_box_message")
        self.notify_box_message.setStyleSheet(DashboardMainWindowStyles.notify_box_style)
        self.notify_box_message.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notify_box.svg"))
        self.notify_box_message.setAlignment(Qt.AlignCenter)

        self.notify_box_notification = QLabel(self.containers)
        self.notify_box_notification.setGeometry(QRect(85, 15, 34, 34))
        self.notify_box_notification.setCursor(QCursor(Qt.PointingHandCursor))
        self.notify_box_notification.setObjectName("notify_box_notification")
        self.notify_box_notification.setStyleSheet(DashboardMainWindowStyles.notify_box_style)
        self.notify_box_notification.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/notify_box.svg"))
        self.notify_box_notification.setAlignment(Qt.AlignCenter)
        
        self.lbl_number_of_message = QLabel(self.containers)
        self.lbl_number_of_message.setGeometry(QRect(140, 20, 31, 21))
        self.lbl_number_of_message.setObjectName("lbl_number_of_message")
        self.lbl_number_of_message.setStyleSheet(DashboardMainWindowStyles.notify_number_of_box_style)
        self.lbl_number_of_notification = QLabel(self.containers)
        self.lbl_number_of_notification.setGeometry(QRect(90, 20, 31, 21))
        self.lbl_number_of_notification.setObjectName("lbl_number_of_notification")
        self.lbl_number_of_notification.setStyleSheet(DashboardMainWindowStyles.notify_number_of_box_style)
      #----------------------------------------------end_notify_message--------------------------------------
      #----------------------------------------------setup_frame_setting-------------------------------------
        self.frame_concat_to_frame_setting = QFrame(self.containers)
        self.frame_concat_to_frame_setting.setGeometry(QRect(1120, 280, 161, 78))
        self.frame_concat_to_frame_setting.setStyleSheet(DashboardMainWindowStyles.all_frame_style)
        self.frame_concat_to_frame_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_setting.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_setting.setObjectName("frame_concat_to_frame_setting")
        self.lbl_close_frame_setting = QLabel(self.frame_concat_to_frame_setting)
        self.lbl_close_frame_setting.setGeometry(QRect(5, 5, 21, 21))
        self.lbl_close_frame_setting.setCursor(QCursor(Qt.PointingHandCursor))

        self.lbl_close_frame_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        self.lbl_close_frame_setting.setObjectName("lbl_close_frame_setting")
        self.card_plugin = QLabel(self.frame_concat_to_frame_setting)
        self.card_plugin.setGeometry(QRect(40, 20, 71, 46))
        self.card_plugin.setCursor(QCursor(Qt.PointingHandCursor))

        self.card_plugin.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_plugin.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_plugin.setObjectName("card_plugin")
        self.pic_plugin_logo = QLabel(self.frame_concat_to_frame_setting)
        self.pic_plugin_logo.setGeometry(QRect(55, 5, 41, 31))
        self.pic_plugin_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_plugin_logo.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        
        self.pic_plugin_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/plugin_icon.svg"))
        self.pic_plugin_logo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_plugin_logo.setObjectName("pic_plugin_logo")
        self.frame_setting = QFrame(self.containers)
        self.frame_setting.setGeometry(QRect(1240, 280, 91, 78))

        self.frame_setting.setStyleSheet(DashboardMainWindowStyles.all_frame_style)

        self.frame_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_setting.setFrameShadow(QFrame.Raised)
        self.lbl_setting = QLabel(self.frame_setting)
        self.lbl_setting.setGeometry(QRect(0, 27, 91, 21))
        self.frame_setting.setObjectName("frame_setting")
        self.lbl_setting.setStyleSheet(DashboardMainWindowStyles.lbl_frames_style)
        self.lbl_setting.setAlignment(Qt.AlignCenter)
        self.lbl_setting.setObjectName("lbl_setting")
        self.lbl_ellipes_setting = QLabel(self.frame_setting)
        self.lbl_ellipes_setting.setGeometry(QRect(0, 43, 91, 21))
        self.lbl_ellipes_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/ellipse_logo.svg"))
        self.lbl_ellipes_setting.setAlignment(Qt.AlignCenter)
        self.lbl_ellipes_setting.setObjectName("lbl_ellipes_setting")
        self.lbl_ellipes_setting.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        #-------------------------------------------------------------------------------------FrameTools

        self.frame_tools = QFrame(self.containers)
        self.frame_tools.setGeometry(QRect(1240, 360, 91, 78))
        self.frame_tools.setStyleSheet(DashboardMainWindowStyles.all_frame_style)
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_tools.setObjectName("frame_tools")
        self.lbl_tools = QLabel(self.frame_tools)
        self.lbl_tools.setGeometry(QRect(0, 27, 91, 21))
        self.lbl_tools.setStyleSheet(DashboardMainWindowStyles.lbl_frames_style)
        self.lbl_tools.setAlignment(Qt.AlignCenter)
        self.lbl_tools.setObjectName("lbl_tools")
        self.lbl_ellipse_tools = QLabel(self.frame_tools)
        self.lbl_ellipse_tools.setGeometry(QRect(0, 43, 91, 21))
        self.lbl_ellipse_tools.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        
        self.lbl_ellipse_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/ellipse_logo.svg"))
        self.lbl_ellipse_tools.setAlignment(Qt.AlignCenter)
        self.lbl_ellipse_tools.setObjectName("lbl_ellipse_tools")
        self.frame_concat_to_frame_tools = QFrame(self.containers)
        self.frame_concat_to_frame_tools.setGeometry(QRect(770, 360, 481, 168))
        self.frame_concat_to_frame_tools.setStyleSheet(DashboardMainWindowStyles.all_frame_style)
        self.frame_concat_to_frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_tools.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_tools.setObjectName("frame_concat_to_frame_tools")
        self.lbl_close_frame_tools = QLabel(self.frame_concat_to_frame_tools)
        self.lbl_close_frame_tools.setGeometry(QRect(5, 5, 21, 21))
        self.lbl_close_frame_tools.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.lbl_close_frame_tools.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        self.lbl_close_frame_tools.setObjectName("lbl_close_frame_tools")
        self.card_forensic = QLabel(self.frame_concat_to_frame_tools)
        self.card_forensic.setGeometry(QRect(25, 25, 71, 46))
        self.card_forensic.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_forensic.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_forensic.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_forensic.setObjectName("card_forensic")
        self.pic_forensic = QLabel(self.frame_concat_to_frame_tools)
        self.pic_forensic.setGeometry(QRect(40, 10, 41, 31))
        self.pic_forensic.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_forensic.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        
        self.pic_forensic.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/forensic_logo.svg"))
        self.pic_forensic.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_forensic.setObjectName("pic_forensic")
        self.card_lot = QLabel(self.frame_concat_to_frame_tools)
        self.card_lot.setGeometry(QRect(112, 25, 71, 46))
        self.card_lot.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_lot.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_lot.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_lot.setObjectName("card_lot")
        self.pic_lot_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_lot_logo.setGeometry(QRect(126, 10, 41, 31))
        self.pic_lot_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_lot_logo.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        
        self.pic_lot_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window//lot_logo.svg"))
        self.pic_lot_logo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_lot_logo.setObjectName("pic_lot_logo")
        self.card_network = QLabel(self.frame_concat_to_frame_tools)
        self.card_network.setGeometry(QRect(286, 25, 71, 46))
        self.card_network.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_network.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_network.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_network.setObjectName("card_network")
        self.pic_Network_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_Network_logo.setGeometry(QRect(300, 10, 41, 31))
        self.pic_Network_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_Network_logo.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
    
        self.pic_Network_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/network_logo.svg"))
        self.pic_Network_logo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_Network_logo.setObjectName("pic_Network_logo")
        self.card_dev_ops = QLabel(self.frame_concat_to_frame_tools)
        self.card_dev_ops.setGeometry(QRect(199, 25, 71, 46))
        self.card_dev_ops.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_dev_ops.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_dev_ops.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_dev_ops.setObjectName("card_dev_ops")
        self.pic_dev_ops_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_dev_ops_logo.setGeometry(QRect(215, 10, 41, 31))
        self.pic_dev_ops_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_dev_ops_logo.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)

        self.pic_dev_ops_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/dev_ops_logo.svg"))
        self.pic_dev_ops_logo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_dev_ops_logo.setObjectName("pic_dev_ops_logo")
        self.card_monitoring = QLabel(self.frame_concat_to_frame_tools)
        self.card_monitoring.setGeometry(QRect(373, 105, 71, 46))
        self.card_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_monitoring.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_monitoring.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_monitoring.setObjectName("card_monitoring")
        self.pic_monitoring_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_monitoring_logo.setGeometry(QRect(388, 90, 41, 31))
        self.pic_monitoring_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_monitoring_logo.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        
        self.pic_monitoring_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/monitoring_logo.svg"))
        self.pic_monitoring_logo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_monitoring_logo.setObjectName("pic_monitoring_logo")
        self.card_web = QLabel(self.frame_concat_to_frame_tools)
        self.card_web.setGeometry(QRect(373, 25, 71, 46))
        self.card_web.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_web.setStyleSheet(DashboardMainWindowStyles.cards_in_frame_style)
        self.card_web.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.card_web.setObjectName("card_web")
        self.pic_web_logo = QLabel(self.frame_concat_to_frame_tools)
        self.pic_web_logo.setGeometry(QRect(388, 10, 41, 31))
        self.pic_web_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_web_logo.setStyleSheet(DashboardMainWindowStyles.transparent_color_style)
        
        self.pic_web_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window//web_logo.svg"))
        self.pic_web_logo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.pic_web_logo.setObjectName("pic_web_logo")
        #-------------------------------------------------------------------------------------
        main_icon = QIcon()
        main_icon.addPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/main_logo.ico"))
        self.setWindowIcon(main_icon)
        self.setAutoFillBackground(False)
        self.setStyleSheet(DashboardMainWindowStyles.main_page_style[1])
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)
        self.centralWidget = QWidget(self)
        self.centralWidget.setStyleSheet(DashboardMainWindowStyles.central_widget_style)
        self.verticalLayout.addWidget(self.containers)
    
        self.setCentralWidget(self.centralwidget)
        # fix on line 34 of main window in kodiak test2
        self.__retranslateUi__()
        
    def __retranslateUi__(self):

        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Kodiak"))
        self.lbl_time.setText("04:20")
        self.lbl_date.setText( "2020/15/19")
        self.location_box.setText( "DevOps")
        self.lbl_number_of_message.setText( "+0")
        self.lbl_number_of_notification.setText("+99")
        self.card_plugin.setText("Add Plugin")
        self.lbl_setting.setText("Setting")
        self.lbl_tools.setText("Tools")
        self.card_forensic.setText("Forensic")
        self.card_lot.setText("lot")
        self.card_network.setText("Network")
        self.card_dev_ops.setText("DevOps")
        self.card_monitoring.setText("Monitoring")
        self.card_web.setText("Web")