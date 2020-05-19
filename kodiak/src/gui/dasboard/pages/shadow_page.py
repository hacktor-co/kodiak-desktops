from PyQt5.QtCore import ( Qt, QPoint )
from PyQt5.QtWidgets import ( QWidget, QVBoxLayout, QGraphicsDropShadowEffect, QDesktopWidget )

class Container(QWidget):
    def __init__(self, window, parent=None):
        super(Container, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        lay = QVBoxLayout(self)
        lay.addWidget(window)
        lay.setContentsMargins(50,50,50,50)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setOffset(0)
        window.setGraphicsEffect(shadow)
        self.center()
        self.oldPos = self.pos()

        from ..components.toolbar_containers.toolbar import ToolBar
        ToolBar().setup_ui( containers = window , parent = self)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()