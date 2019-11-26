
def delete_items_of_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                delete_items_of_layout(item.layout())

def box_delete(layout):
    for i in range(layout.count()):
        layout_item = layout.itemAt(i)
        # if layout_item.layout() == box:
        delete_items_of_layout(layout_item.layout())
        # self.vlayout.removeItem(layout_item)
        # break
