
from PyQt5.QtCore import (
    QEvent, pyqtSignal,
    QObject
)

class UtilsClick:
    @staticmethod
    def clickable(widget): 
        class Filter(QObject):
            clicked =pyqtSignal()  
            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True             
                return False
        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked
