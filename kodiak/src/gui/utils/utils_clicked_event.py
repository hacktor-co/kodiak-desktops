"""
    - Created on May 17/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtCore import (
    QEvent, pyqtSignal,
    QObject, Qt
)


class UtilsClick:
    @staticmethod
    def clickable(widget):

        """this class for when object clicked 

        Arguments:
            widget {Qobject}

        Returns:
            [filter]
        """

        class Filter(QObject):
            clicked = pyqtSignal()

            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            if event.button() == Qt.LeftButton:
                                self.clicked.emit()
                                # The developer can opt for .emit(obj) to get the object within the slot.
                                return True
                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked
