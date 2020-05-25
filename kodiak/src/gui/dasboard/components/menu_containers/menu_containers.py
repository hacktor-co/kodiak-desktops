"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
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
from ....utils.utils_clicked_event import UtilsClick

from functools import partial


class MenuContainers:

    def __init__(self):
        super(MenuContainers, self).__init__()

    def setup_ui(self, vertical_layoutwidget: QVBoxLayout, containers: QFrame, contaners_item: QFrame):

        self.containers_menu_li = QVBoxLayout(vertical_layoutwidget)
        self.containers_menu_li.setContentsMargins(0, 0, 0, 0)
        self.containers_menu_li.setSpacing(23)
        self.containers_menu_li.setObjectName("containers_menu_li")

        # set li_setting
        li_setting = QLabel(vertical_layoutwidget)
        li_setting.setAccessibleName(MenuContainersStyles.lis_style[0])
        li_setting.setStyleSheet(MenuContainersStyles.lis_style[1])
        li_setting.setCursor(QCursor(Qt.PointingHandCursor))
        li_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/setting_logo.svg"))
        li_setting.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        UtilsClick.clickable(li_setting).connect(partial(self.li_clicked, "setting"))
        self.containers_menu_li.addWidget(li_setting)

        # set li_menu
        li_menu = QLabel(vertical_layoutwidget)
        li_menu.setCursor(QCursor(Qt.PointingHandCursor))
        li_menu.setAccessibleName(MenuContainersStyles.lis_style[0])
        li_menu.setStyleSheet(MenuContainersStyles.lis_style[1])
        li_menu.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/menu_logo.svg"))
        li_menu.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        UtilsClick.clickable(li_menu).connect(partial(self.li_clicked, "menu"))
        self.containers_menu_li.addWidget(li_menu)

        # set li_report
        li_report = QLabel(vertical_layoutwidget)
        li_report.setCursor(QCursor(Qt.PointingHandCursor))
        li_report.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/chart_logo.svg"))
        li_report.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        li_report.setAccessibleName(MenuContainersStyles.lis_style[0])
        li_report.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.containers_menu_li.addWidget(li_report)

        # set li_store
        li_store = QLabel(vertical_layoutwidget)
        li_store.setAccessibleName(MenuContainersStyles.lis_style[0])
        li_store.setStyleSheet(MenuContainersStyles.lis_style[1])
        li_store.setCursor(QCursor(Qt.PointingHandCursor))
        li_store.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/box_logo.svg"))
        li_store.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(li_store)

        # set li_brain
        li_brain = QLabel(vertical_layoutwidget)
        li_brain.setAccessibleName(MenuContainersStyles.lis_style[0])
        li_brain.setStyleSheet(MenuContainersStyles.lis_style[1])
        li_brain.setCursor(QCursor(Qt.PointingHandCursor))
        li_brain.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/brain_logo.svg"))
        li_brain.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(li_brain)

        from .settings_dialog_frame.setting_dialog_frame import SettingDialogFrame
        self.setting_Dialog = SettingDialogFrame()
        self.setting_Dialog.setup_ui(containers)
        self.setting_Dialog.set_visibility_effect(False, False)

        from .tools_dialog_frame.tool_dialog_frame import ToolDialogFrame
        self.tools_dialog = ToolDialogFrame(containers)
        self.tools_dialog.setup_ui(containers_item=contaners_item)
        self.tools_dialog.set_visibility_effect(False, False)

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
