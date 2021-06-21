from artech_gui.geometrie.AT_Rectange import AT_Rectangle
from artech_gui.application.AT_IApp import AT_IApp
from artech_gui.widget.AT_Text import AT_Text
from artech_gui.maths.AT_Coord import *
from artech_gui.maths.AT_ITransform import *

from pygame.locals import *

class AT_Button(AT_IApp, AT_ITransform):
    def __init__(self):
        self.__rectangleBouton = AT_Rectangle()
        self.__textBouton = AT_Text()
        self.__textBouton.setText("Click Me")
        self.__drawText = AT_Text()
        self.__drawText.setText(self.__textBouton.getText())

        self.__rectangleBouton.setSize(Size2D(200, 60))

        self.__boutonAction = {}

        self.__boutonAction["normal"] = [Color(33, 150, 243), Color(200, 200, 200), None, True]
        self.__boutonAction["hover"] = [Color(30, 136, 229), Color(200, 200, 200), None, True]
        self.__boutonAction["pressed"] = [Color(25, 118, 210), Color(200, 200, 200), None, True]
        self.__boutonAction["disable"] = [Color(64, 64, 64), Color(200, 200, 200), None, True]

        self.__actualAction = "normal"
        self.__confineText()

        self.__borderSize = 1
        self.__borderRadius = 3

        self.__rectangleBouton.setBorderRadius(self.__borderRadius)
        self.__rectangleBouton.setBorder(self.__borderSize)
        self.__updateAction()

    def setAction(self, name, callBack):
        if name in self.__boutonAction:
            self.__boutonAction[name][2] = callBack

    def setActionColor(self, name, bgColor, bdColor):
        if name in self.__boutonAction:
            self.__boutonAction[name][0] = bgColor
            self.__boutonAction[name][1] = bdColor

    def __updateAction(self):
        self.__rectangleBouton.setBgColor(self.__boutonAction[self.__actualAction][0])
        self.__rectangleBouton.setBdColor(self.__boutonAction[self.__actualAction][1])

    def updateEvent(self, event):
        action = self.__actualAction
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                action = "pressed"
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if self.__rectangleBouton.isContain(Vector2D(event.pos[0], event.pos[1])) == True:
                    action = "hover"
                else:
                    action = "normal"
        elif event.type == MOUSEMOTION:
            if self.__rectangleBouton.isContain(Vector2D(event.pos[0], event.pos[1])) == True:
                action = "hover"
            else:
                action = "normal"

        if action != self.__actualAction:
            self.__actualAction = action
            self.__updateAction()
            if self.__boutonAction[self.__actualAction][2] != None:
                self.__boutonAction[self.__actualAction][2](event)

    def draw(self, screen):
        self.__rectangleBouton.draw(screen)
        self.__drawText.draw(screen)

    def setPosition(self, position):
        self.__rectangleBouton.setPosition(position)
        self.__confineText()

    def getPosition(self):
        return self.__rectangleBouton.getPosition()

    def __confineText(self):
        w = self.__rectangleBouton.getSize().getW()
        h = self.__rectangleBouton.getSize().getH()

        if self.__drawText.getSize().getW() >= self.__rectangleBouton.getSize().getW():
            w = self.__drawText.getSize().getW() + 10
        if self.__drawText.getSize().getH() >= self.__rectangleBouton.getSize().getH():
            h = self.__drawText.getSize().getH() + 10

        self.__rectangleBouton.setSize(Size2D(w, h))

        x = self.__rectangleBouton.getPosition().getX() + (self.__rectangleBouton.getSize().getW() - self.__drawText.getSize().getW())/2
        y = self.__rectangleBouton.getPosition().getY() + (self.__rectangleBouton.getSize().getH() - self.__drawText.getSize().getH())/2

        self.__drawText.setPosition(Vector2D(x, y))

    def setFontName(self, name):
        self.__textBouton.setFontName(name)
        self.__drawText.setFontName(name)
        self.__confineText()

    def setFontSize(self, size):
        self.__textBouton.setFontSize(size)
        self.__drawText.setFontSize(size)
        self.__confineText()

    def getFontSize(self):
        return self.__textBouton.getFontSize()

    def getFontName(self):
        return self.__textBouton.getFontName()