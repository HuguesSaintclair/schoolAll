from pygame.locals import *

class AT_Scene():
    id = 0
    def __init__(self, parent):
        from artech_gui.application.AT_APP import AT_Application
        if issubclass(type(parent), AT_Application) or isinstance(type(parent), AT_Application):
            self.__parent = parent

        AT_Scene.id += 1
        self.__id = AT_Scene.id
        self.__name = "Scene_{}".format(self.__id)

        self.__background = {"color": Color(255, 255, 255), "image": None}
        self.__backgroundType = "color"

        self.__id = 0
        self.__name = ""

    def getParent(self):
        return self.__parent

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def updateEvent(self, event):
        pass

    def draw(self, screen):
        if self.__backgroundType == "color":
            screen.fill(self.__background[self.__backgroundType])

    def update(self, screen):
        pass

    def setBackground(self, **infos):
        for name, value in infos.items():
            if name.lower() == "color":
                self.__backgroundType = "color"
                self.__background[self.__backgroundType] = value
#from artech_gui.application.artech_application import AT_Application