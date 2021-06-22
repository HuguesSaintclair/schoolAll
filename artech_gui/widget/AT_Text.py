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

        self.__backgroundImage = None
        self.__italic = False
        self.__bold = False
        self.__underline = False

        self.__charPositions = []
        self.__initFont()

        self.__background = False
        self.__area = self.__text_draw.get_rect()

    def activateBg(self, activate_or_desactivate):
        self.__background = activate_or_desactivate

    def isBgActivate(self):
        return self.__background

    def __initFont(self):
        self.__font = pygame.font.Font(self.__fontName, self.__fontSize)
        self.__font.set_bold(self.__bold)
        self.__font.set_italic(self.__italic)
        self.__font.set_underline(self.__underline)
        self.__text_draw = self.__font.render(self.__text, True, self.__color, self.__backgroundImage)
        self.__size = Size2D(w=self.__text_draw.get_rect().w, h=self.__text_draw.get_rect().h)
        self.__rectangle.setSize(self.__size)

        self.__setCharPositions()
        self.__area = self.__text_draw.get_rect()

    def getArea(self):
        return self.__area

    def setArea(self, x, y, w, h):
        if x != None:
            self.__area.x = x
        if y != None:
            self.__area.y = y
        if w != None:
            self.__area.w = w
        if h != None:
            self.__area.h = h

    def __setCharPositions(self):
        self.__charPositions.clear()
        self.__charPositions = []
        for i in range(len(self.__text)):
            w, h = self.__font.size(self.__text[:i + 1])
            self.__charPositions.append(w)

    def getCharIndex(self, position):
        for i, pos in enumerate(self.__charPositions):
            if position <= pos:
                return i
        return i

    def getWidth(self, index):
        if index >= 0 and index < len(self.__text):
            return self.__charPositions[index]
        return 0

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
        screen.blit(self.__text_draw, (self.__position.getX(), self.__position.getY()), area=self.__area)

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

    def setColor(self, color):
        self.__color = color
        self.__initFont()

    def getColor(self):
        return self.__color

    def __str__(self):
        return "Text({}, {})".format(self.__position, self.__size)