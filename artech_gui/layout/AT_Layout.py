from artech_gui.maths.AT_Coord import Vector2D, Size2D
from artech_gui.maths.AT_ITransform import AT_ITransform
from artech_gui.application.AT_IApp import AT_IApp

class AT_Layout(AT_IApp, AT_ITransform):
    def __init__(self):
        self.__layout = []
        self.__widget = []
        self.__position = Vector2D()
        self.__size = Size2D()
        self.__parent = None

    def addWidget(self, widget, wAdapt, hAdapt):
        widget.setParent(self)
        self.__widget.append([widget, wAdapt, hAdapt])

    def setParent(self, parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

    def removeWidget(self, widget):
        for w in self.__widget:
            if w[0] == widget:
                self.__widget.remove(w)

    def addLayout(self, layout, wAdapt, hAdapt):
        layout.setParent(self)
        self.__widget.append([layout, wAdapt, hAdapt])

    def removeLayout(self, layout):
        for w in self.__layout:
            if w[0] == layout:
                self.__layout.remove(w)

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def getRelativeSize(self):
       pass

    def organize(self):
        pass

    def updateEvent(self, event):
        for layout in self.__layout:
            layout[0].updateEvent(event)

        for widget in self.__widget:
            widget[0].updateEvent(event)

    def update(self, scene):
        for layout in self.__layout:
            if layout[0].getParent() != self:
                self.removeLayout(layout)
        for layout in self.__layout:
            layout.update(scene)
        for widget in self.__widget:
            if widget[0].getParent() != self:
                self.removeLayout(widget)
        for widget in self.__widget:
            widget.update(scene)
