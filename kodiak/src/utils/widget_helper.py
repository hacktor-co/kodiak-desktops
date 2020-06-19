

class WidgetHelper:

    @staticmethod
    def delete_items_of_layout(layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    delete_items_of_layout(item.layout())

    def box_delete(self, layout):
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            self.delete_items_of_layout(layout_item.layout())

    def delete_all_widget(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)