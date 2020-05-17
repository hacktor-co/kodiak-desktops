"""

"""

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel, QFrame
)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)
from PyQt5.QtCore import Qt

from .menu_containers_style import MenuContainersStyles
from commons.constants.app_paths import AppPaths
from  ....utils.utils_clicked_event import UtilsClick

from functools import partial

class MenuContainers:

    def __init__(self):
        super(MenuContainers, self).__init__()

    def setup_ui(self, verticalLayoutWidget: QVBoxLayout, containers: QFrame):
        self.containers_menu_li = QVBoxLayout(verticalLayoutWidget)
        self.containers_menu_li.setContentsMargins(0, 0, 0, 0)
        self.containers_menu_li.setSpacing(23)
        self.containers_menu_li.setObjectName("containers_menu_li")
        #set li_setting
        self.li_setting = QLabel(verticalLayoutWidget)
        self.li_setting.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_setting.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/setting_logo.svg"))
        self.li_setting.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_setting)
        
        #set li_menu
        self.li_menu = QLabel(verticalLayoutWidget)
        self.li_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_menu.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_menu.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_menu.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/menu_logo.svg"))
        self.li_menu.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_menu)
        
        #set li_chart
        self.li_chart = QLabel(verticalLayoutWidget)
        self.li_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_chart.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/chart_logo.svg"))
        
        self.li_chart.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.li_chart.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_chart.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.containers_menu_li.addWidget(self.li_chart)
        
        #set li_box
        self.li_box = QLabel(verticalLayoutWidget)
        self.li_box.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_box.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_box.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/box_logo.svg"))
        
        self.li_box.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_box)
        
        #set li_brain
        self.li_brain = QLabel(verticalLayoutWidget)
        self.li_brain.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_brain.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_brain.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_brain.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/brain_logo.svg"))
        
        self.li_brain.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_brain)

        from .settings_dialog_frame.setting_dialog_frame import SettingDialogFrame
        self.setting_Dialog = SettingDialogFrame()
        self.setting_Dialog.setup_ui(containers)

        from .tools_dialog_frame.tool_dialog_frame import ToolDialogFrame
        self.tools_dialog = ToolDialogFrame()
        self.tools_dialog.setup_ui(containers)

        self.tools_dialog.set_visibility_effect(False,False)
        #Call Events
        UtilsClick.clickable(self.li_setting).connect(partial(self.li_clicked, "setting"))
        UtilsClick.clickable(self.li_menu).connect(partial(self.li_clicked, "menu"))

    def li_clicked(self, li_name: str):
        
        if li_name == "setting":
            self.hide_all_frame()
            self.setting_Dialog.set_visibility_effect(True, True)

        elif li_name == "menu":
            self.hide_all_frame()
            self.tools_dialog.set_visibility_effect(True, True)

    def hide_all_frame(self):
        """this method for hide all frames
        """
        self.setting_Dialog.set_visibility_effect(False, False)
        self.tools_dialog.set_visibility_effect(False, False)

