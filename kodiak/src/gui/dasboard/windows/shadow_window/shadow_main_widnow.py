from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QGraphicsDropShadowEffect, QDesktopWidget,
    QFrame, QGridLayout
)


class Container(QWidget):
    def __init__(self, window, parent=None, containers: QFrame = None, containers_gridlayout: QGridLayout = None):
        super(Container, self).__init__(parent)
        self.window = window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(window.x()+50, window.y()+50, window.width()+50, window.height()+50)
        self.lay = QVBoxLayout(self)
        self.lay.addWidget(window)
        self.lay.setContentsMargins(50, 50, 50, 50)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setOffset(0)
        self.window.setGraphicsEffect(shadow)
        self.center()
        self.oldPos = self.pos()
        self.pressing: bool = False

        from ...components.toolbar_containers.toolbar import ToolBar
        self.toolbar = ToolBar(main_page=window, parent=self)
        self.toolbar.setup_ui(containers=containers)
        containers_gridlayout.addWidget(self.toolbar, 0, 0, 1, 3)

    def center(self):
        """this method main set location from center of the desktop
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())