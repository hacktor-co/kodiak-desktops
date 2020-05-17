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


class MenuContainers:

    def __init__(self):
        super(MenuContainers, self).__init__()

    def setup_ui(self, verticalLayoutWidget: QVBoxLayout, containers: QFrame):
        self.containers_menu_li = QVBoxLayout(verticalLayoutWidget)
        self.containers_menu_li.setContentsMargins(0, 0, 0, 0)
        self.containers_menu_li.setSpacing(23)
        self.containers_menu_li.setObjectName("containers_menu_li")

        self.li_setting = QLabel(verticalLayoutWidget)
        self.li_setting.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_setting.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/setting_logo.svg"))
        self.li_setting.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_setting)

        self.li_menu = QLabel(verticalLayoutWidget)
        self.li_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_menu.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_menu.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_menu.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/menu_logo.svg"))
        self.li_menu.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_menu)

        self.li_chart = QLabel(verticalLayoutWidget)
        self.li_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_chart.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/chart_logo.svg"))
        self.li_chart.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.li_chart.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_chart.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.containers_menu_li.addWidget(self.li_chart)

        self.li_box = QLabel(verticalLayoutWidget)
        self.li_box.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_box.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_box.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/box_logo.svg"))
        self.li_box.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_box)

        self.li_brain = QLabel(verticalLayoutWidget)
        self.li_brain.setAccessibleName(MenuContainersStyles.lis_style[0])
        self.li_brain.setStyleSheet(MenuContainersStyles.lis_style[1])
        self.li_brain.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_brain.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/brain_logo.svg"))
        self.li_brain.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.containers_menu_li.addWidget(self.li_brain)

        from .tools_dialog_frame.tool_dialog_frame import ToolDialogFrame
        ToolDialogFrame().setup_ui(containers)

        from .settings_dialog_frame.setting_dialog_frame import SettingDialogFrame
        SettingDialogFrame().setup_ui(containers)
