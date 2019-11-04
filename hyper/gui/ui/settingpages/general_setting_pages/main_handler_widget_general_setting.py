"""
    - Created on Nov 2/2019 - hacktorco
    - All rights reserved for hacktor team

    - this widget set all controls that must exist in general setting of hyper
"""

from functools import partial

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QScrollArea, QFrame,
    QPushButton, QFormLayout, QGroupBox, QVBoxLayout,
)

from common.constants.consts import (
    DEFINE_PLUGIN_TOOLS_PATH, DEFINE_PLUGIN_TOOLSBOX_PATH
)
from common.utils.pwd_helper import (
    get_all_directory, GET_CWD
)
from gui.ui.toolsboxpage.tools_scroll_widget import ToolsScrollWidget
from gui.common.styles.settingpages.main_handler_widget_general_setting_style import *
from common.utils.os_helper import get_os_info


class MainHandlerWidgetGeneralSetting(QWidget):
    def __init__(self, parent):
        super(MainHandlerWidgetGeneralSetting, self).__init__(parent)
        self.setAccessibleName(main_widget_style[0])

        self.setLayoutDirection(Qt.RightToLeft)

        if get_os_info()["os"] == "Windows":
            self.setStyleSheet(main_widget_style_windows[1])
        else:
            self.setStyleSheet(main_widget_style[1])

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 0, 20, 27)
        self.layout.addStretch()

        icon_holder = QLabel()
        image = QPixmap('./gui/assets/general_setting_header_label_icon.svg')

        icon_holder.setPixmap(image)
        icon_holder.setAccessibleName(general_setting_label[0])
        icon_holder.setStyleSheet(general_setting_label[1])

        self.layout.addWidget(icon_holder)

        self.layout.addLayout(self.__add_menu_items__())

        self.setLayout(self.layout)

    def __add_list_header_section__(self) -> QVBoxLayout:
        menu_list_header_layout = QVBoxLayout()
        menu_list_header_layout.addStretch()
        menu_list_header_layout.setContentsMargins(0, 0, 0, 0)

        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignBottom)

        group_box = QGroupBox()
        group_box.setAccessibleName(menu_general_setting_header_list_group_style[0])
        group_box.setStyleSheet(menu_general_setting_header_list_group_style[1])
        group_box.setContentsMargins(0, 0, 0, 0)

        btn_plugin_manager = QPushButton("Plugins")
        btn_plugin_manager.setAccessibleName(menu_general_setting_header_list_btn_style[0])
        btn_plugin_manager.setStyleSheet(menu_general_setting_header_list_btn_style[1])

        def show_plugins_setting_widgets(parent):
            from gui.ui.settingpages.general_setting_pages.general_setting_plugin_manager \
                import PluginManagerGeneralSetting

            plugin_manager_page = PluginManagerGeneralSetting()
            parent.selected_form_layout.addLayout(plugin_manager_page.get_layout())

        btn_plugin_manager.clicked.connect(partial(show_plugins_setting_widgets, self))

        form_layout.addWidget(btn_plugin_manager)

        group_box.setLayout(form_layout)

        scroll_area = QScrollArea()
        scroll_area.setContentsMargins(0, 0, 0, 0)
        scroll_area.setAccessibleName(scroll_area_menu_general_list_header_style[0])
        scroll_area.setStyleSheet(scroll_area_menu_general_list_header_style[1])

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidget(group_box)

        menu_list_header_layout.addWidget(scroll_area)

        return menu_list_header_layout

    def __add_selected_page_menu_items__(self) -> QVBoxLayout:

        menu_list_header_layout = QVBoxLayout()
        menu_list_header_layout.addStretch()
        menu_list_header_layout.setContentsMargins(0, 0, 0, 0)
        menu_list_header_layout.setAlignment(Qt.AlignTop)

        fram_layout = QFrame()
        fram_layout.setAccessibleName(menu_general_setting_list_group_style[0])
        fram_layout.setStyleSheet(menu_general_setting_list_group_style[1])
        fram_layout.setContentsMargins(0, 0, 0, 0)
        fram_layout.setLayoutDirection(Qt.LeftToRight)

        self.selected_form_layout = QVBoxLayout()
        self.selected_form_layout.setAlignment(Qt.AlignBottom)
        self.selected_form_layout.setContentsMargins(0, 0, 0, 0)
        self.selected_form_layout.addStretch()

        fram_layout.setLayout(self.selected_form_layout)

        menu_list_header_layout.addWidget(fram_layout)

        return menu_list_header_layout

    def __add_menu_items__(self):
        menu_items_layout = QHBoxLayout()

        menu_items_layout.addStretch()
        menu_items_layout.setContentsMargins(0, 0, 0, 0)

        menu_items_layout.addLayout(self.__add_selected_page_menu_items__())
        menu_items_layout.addLayout(self.__add_list_header_section__())

        return menu_items_layout
