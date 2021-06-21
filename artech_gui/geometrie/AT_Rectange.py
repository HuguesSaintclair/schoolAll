from artech_gui.maths.AT_Coord import Vector2D, Size2D
from artech_gui.application.AT_IApp import AT_IApp
from artech_gui.maths.AT_ITransform import AT_ITransform
from pygame.locals import *
import pygame

class AT_Rectangle(AT_IApp, AT_ITransform):
    def __init__(self):
        self.__position = Vector2D()
        self.__size = Size2D()

        self.__borderColor = Color(0, 0, 0, 0)
        self.__border = 0
        self.__backgroundColor = Color(255, 255, 255, 255)

        self.__center = Vector2D()
        self.__borderRadius = 0

    def draw(self, screen):
        x = self.__position.getX() - self.__center.getX()
        y = self.__position.getY() - self.__center.getY()

        pygame.draw.rect(screen, color=self.__backgroundColor, rect = (x, y, self.__size.getW(), self.__size.getH()), border_radius=self.__borderRadius)
        if self.__border > 0:
            pygame.draw.rect(screen, color=self.__borderColor, rect=(x, y, self.__size.getW(), self.__size.getH()), width=self.__border, border_radius=self.__borderRadius)

    def betBorderRadius(self):
        return self.__borderRadius

    def setBorderRadius(self, value):
        self.__borderRadius = value

    def getBorder(self):
        return self.__border

    def setBorder(self, value):
        self.__border = value

    def getBgColor(self):
        return self.__backgroundColor

    def setBgColor(self, value):
        self.__backgroundColor = value

    def getBdColor(self):
        return self.__borderColor

    def setBdColor(self, value):
        self.__borderColor = value

    def getPosition(self):
        return Vector2D(self.__position.getX(), self.__position.getY())

    def getCenter(self):
        return Vector2D(self.__center.getX(), self.__center.getY())

    def setCenter(self, center):
        self.__center.setX(center.getX())
        self.__center.setY(center.getY())

    def getSize(self):
        return Size2D(self.__size.getW(), self.__size.getH())

    def setPosition(self, position):
        self.__position.setX(position.getX())
        self.__position.setY(position.getY())

    def setSize(self, size):
        self.__size.setW(size.getW())
        self.__size.setH(size.getH())

    def __str__(self):
        return "Rectangle({}, {})".format(self.__position, self.__size)

    def isContain(self, value):
        if type(value) == Vector2D:
            if value.getX() >= 0 and self.getPosition().getX() + self.getSize().getW() > value.getX() and \
               value.getY() >= 0 and self.getPosition().getY() + self.getSize().getH() > value.getY():
                return True
            return False
        return False