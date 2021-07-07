from artech_gui.maths.AT_Coord import Vector2D, Size2D
from artech_gui.maths.AT_ITransform import AT_ITransform
from artech_gui.application.AT_IApp import AT_IApp

from AT_Layout import AT_Layout

class AT_VLayout(AT_Layout):
    def __init__(self):
        super.__init__()

    def draw(self, screen):
        for widget in self.__widget:
            widget.draw(screen)

        for layout in self.__layout:
            layout.draw(screen)

    def getRelativeSize(self):
        size = Size2D()
        for widget in self.__widget:
            pass

    def organize(self):
        pass