from artech_gui.maths.AT_Coord import Vector2D, Size2D
from artech_gui.maths.AT_ITransform import AT_ITransform
from artech_gui.application.AT_IApp import AT_IApp
from artech_gui.geometrie.AT_Rectange import AT_Rectangle
import pygame
from pygame.locals import *

class AT_Text(AT_IApp, AT_ITransform):
    def __init__(self):
        self.__color = Color(255, 255, 255, 255)
        self.__text = "ARTECH_GUI"

        self.__fontSize = 20
        self.__fontName = None
        self.__position = Vector2D()
        self.__rectangle = AT_Rectangle()

        self.__initFont()

        self.__background = False

    def activateBg(self, activate_or_desactivate):
        self.__background = activate_or_desactivate

    def isBgActivate(self):
        return self.__background

    def __initFont(self):
        self.__font = pygame.font.Font(self.__fontName, self.__fontSize)
        self.__text_draw = self.__font.render(self.__text, True, self.__color)
        self.__size = Size2D(w=self.__text_draw.get_rect().w, h=self.__text_draw.get_rect().h)
        self.__rectangle.setSize(self.__size)

    def getFontName(self):
        return self.__fontName

    def setFontName(self, name):
        self.__fontName = name
        self.__initFont()

    def getFontSize(self):
        return self.__fontSize

    def setFontSize(self, size):
        self.__fontSize = size
        self.__initFont()

    def setText(self, text):
        self.__text = text
        self.__initFont()

    def getText(self):
        return self.__text

    def draw(self, screen):
        if self.__background:
            self.__rectangle.draw(screen)
        screen.blit(self.__text_draw, (self.__position.getX(), self.__position.getY()))

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__size

    def setPosition(self, position):
        self.__position = position
        self.__rectangle.setPosition(position)

    def setSize(self, size):
        self.__size = size
        self.__rectangle.setSize(size)
        self.__text_draw = pygame.transform.smoothscale(self.__text_draw, (size.getW(), size.getH()))

    def getBgColor(self):
        return self.__rectangle.getBgColor()

    def setBgColor(self, value):
        self.__rectangle.setBgColor(value)

    def __str__(self):
        return "Text({}, {})".format(self.__position, self.__size)