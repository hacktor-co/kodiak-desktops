
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)

class ToolsBoxScrollWidget(QWidget):
    def __init__(self, parent=None):
        super(ToolsBoxScrollWidget, self).__init__(parent)

        self.setStyleSheet(
            """
                background-color: red;
                position: absolute;
                left: 400px;
                top: 10px;
            """
        )
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignRight)

        label = QLabel("Hell this is test for scroll view")
        layout.addWidget(label)
        self.setLayout(layout)
