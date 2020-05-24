"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QLabel, QFrame
)
from PyQt5.QtGui import (
    QIcon, QPixmap,
    QCursor
)
from PyQt5.QtCore import (
    Qt, QSize,
    QRect, QCoreApplication
)

from .devops_containers_style import DevopsContainersStyles


class DevopsContainers:
    def __init__(self):
        super(DevopsContainers, self).__init__()

    def setup_ui(self, containers: QFrame):
        # ---------------------------------------------------------------------- dev_op_containers
        self.dev_op_containers = QFrame(containers)
        self.dev_op_containers.setGeometry(QRect(50, 30, 1264, 750))
        self.dev_op_containers.setFrameShape(QFrame.StyledPanel)
        self.dev_op_containers.setFrameShadow(QFrame.Raised)
        self.dev_op_containers.setObjectName("dev_op_containers")
        # ------------------------------------------------------------------------ Add Parts
        from .devops_registered_part.devops_registered import DevopsRegistered
        DevopsRegistered().setup_ui(containers=self.dev_op_containers)
        from .devops_unregistered_part.devops_unregistered import DevopsUnregistered
        DevopsUnregistered().setup_ui(containers=self.dev_op_containers)
        # ----------------------------------------------------------------------lbl_registered
        self.lbl_registered = QLabel(self.dev_op_containers)
        self.lbl_registered.setGeometry(QRect(30, 80, 111, 32))
        self.lbl_registered.setMinimumSize(QSize(91, 32))
        self.lbl_registered.setObjectName(DevopsContainersStyles.lbl_registered_style[0])
        self.lbl_registered.setStyleSheet(DevopsContainersStyles.lbl_registered_style[1])
        self.lbl_registered.setAlignment(Qt.AlignCenter)
        # ----------------------------------------------------------------------lbl_unregistered
        self.lbl_unregistered = QLabel(self.dev_op_containers)
        self.lbl_unregistered.setGeometry(QRect(30, 425, 141, 32))
        self.lbl_unregistered.setMinimumSize(QSize(91, 32))
        self.lbl_unregistered.setObjectName(DevopsContainersStyles.lbl_unregistered_style[0])
        self.lbl_unregistered.setStyleSheet(DevopsContainersStyles.lbl_unregistered_style[1])
        self.lbl_unregistered.setAlignment(Qt.AlignCenter)
        # ----------------------------------------------------------------------lbl_title
        self.lbl_title = QLabel(self.dev_op_containers)
        self.lbl_title.setGeometry(QRect(441, 10, 281, 16))
        self.lbl_title.setObjectName(DevopsContainersStyles.lbl_title_style[0])
        self.lbl_title.setStyleSheet(DevopsContainersStyles.lbl_title_style[1])
        # ----------------------------------------------------------------------
        self.retranslate_ui()
        self.set_visibility_effect(False)

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.lbl_registered.setText(_translate("Form", "REGISTERED"))
        self.lbl_unregistered.setText(_translate("Form", "UNREGISTERED"))
        self.lbl_title.setText(_translate("Form", "Here is your devops addons to use "))

    def set_visibility_effect(self, visible: bool):
        self.dev_op_containers.setVisible(visible)
