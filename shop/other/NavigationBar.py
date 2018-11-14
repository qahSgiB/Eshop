class NavigationBarItem():
    def __init__(self, text, viewName):
        self.text = text
        self.viewName = viewName

class NavigationBar():
    def __init__(self, itemClass=NavigationBarItem):
        self.items = []
        self.itemClass = itemClass

    def addItem(self, *args, **params):
        self.items.append(self.itemClass(*args, **params))
