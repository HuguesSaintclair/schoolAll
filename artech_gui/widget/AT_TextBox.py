from artech_gui.widget.AT_Text import AT_Text
from artech_gui.geometrie.AT_Rectange import AT_Rectangle
from artech_gui.maths.AT_Coord import Vector2D, Size2D
from artech_gui.maths.AT_ITransform import AT_ITransform
from artech_gui.application.AT_IApp import AT_IApp

import pygame
from pygame.locals import *
import time

class AT_TextBox(AT_IApp, AT_ITransform):
    def __init__(self):
        self.__defaultTextColor = Color(175, 175, 175)
        self.__normalTextColor = Color(50, 50, 50)

        self.__textEditAction = {}

        self.__textEditAction["normal"] = [Color(255, 255, 255), Color(200, 200, 200), None, True]
        self.__textEditAction["hover"] = [Color(255, 255, 255), Color(157, 225, 255), None, True]
        self.__textEditAction["pressed"] = [Color(255, 255, 255), Color(157, 225, 255), None, True]
        self.__textEditAction["disable"] = [Color(255, 255, 255), Color(200, 200, 200), None, True]
        self.__textEditAction["textChange"] = [Color(255, 255, 255), Color(157, 225, 255), None, True]

        self.__actualAction = "normal"

        self.__borderSize = 1
        self.__borderRadius = 3

        self.__rectangleTextEdit = AT_Rectangle()
        self.__textInfos = AT_Text()
        self.__textInfos.setColor(self.__defaultTextColor)
        self.__defaultText = "Enter Text"
        self.__textInfos.setText(self.__defaultText)
        self.__textInfos.setFontSize(30)

        self.__rectangleTextEdit.setBorderRadius(self.__borderRadius)
        self.__rectangleTextEdit.setBorder(self.__borderSize)

        self.__updateAction()

        self.__rectangleTextEdit.setSize(Size2D(300, 40))

        self.__writent = False
        self.__contentWrite = False
        self.__cursor = Rect(5, 5, 2, 0)
        self.__caracterCurseurPosition = 0
        self.__confineText()
        self.__cursor = Rect(5, 5, 2, self.__textInfos.getSize().getH())

    def setParent(self, parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

    def __updateAction(self):
        self.__rectangleTextEdit.setBgColor(self.__textEditAction[self.__actualAction][0])
        self.__rectangleTextEdit.setBdColor(self.__textEditAction[self.__actualAction][1])

    def __confineText(self):
        w = self.__rectangleTextEdit.getSize().getW()
        h = self.__rectangleTextEdit.getSize().getH()

        if self.__textInfos.getSize().getH() >= self.__rectangleTextEdit.getSize().getH():
            h = self.__textInfos.getSize().getH() + 10

        self.__rectangleTextEdit.setSize(Size2D(w, h))

        x = self.__rectangleTextEdit.getPosition().getX() + 5
        y = self.__rectangleTextEdit.getPosition().getY() + (self.__rectangleTextEdit.getSize().getH() - self.__textInfos.getSize().getH())/2

        self.__textInfos.setPosition(Vector2D(x, y))

    def __recalculateCursorPosition(self, cursorPosition):
        x1 = 0
        if self.__contentWrite and self.__rectangleTextEdit.getSize().getW() - 10 < self.__textInfos.getSize().getW():
            x1 = self.__textInfos.getSize().getW() - self.__rectangleTextEdit.getSize().getW() + 10

        w1 = 0
        #print(cursorPosition)
        if cursorPosition == 0:
            w1 = 0
            x1 = 0
        elif self.__contentWrite == True:
            w1 = self.__textInfos.getWidth(len(self.__textInfos.getText()) - 1)
            if self.__contentWrite == False or w1 == None:
                w1 = 0
            if cursorPosition == len(self.__textInfos.getText()):
                if w1 >= self.__rectangleTextEdit.getSize().getW() - 10:
                    w1 = self.__rectangleTextEdit.getSize().getW() - 10
            else:
                w2 = self.__textInfos.getWidth(cursorPosition - 1)
                w1 = w2 - x1
                if w1 < 0:
                    w1 = 0
                    x1 = w2 if cursorPosition > 0 else 0
                elif w1 > 0:
                    pass

        self.__cursor.x = self.__rectangleTextEdit.getPosition().getX() + 5 + w1
        self.__cursor.y = self.__textInfos.getPosition().getY()
        self.__cursor.height = self.__textInfos.getSize().getH()

        self.__textInfos.setArea(x1, 0, self.__rectangleTextEdit.getSize().getW() - 10,
                                self.__rectangleTextEdit.getSize().getH() - 10)

    def setAction(self, name, callBack):
        if name in self.__textEditAction:
            self.__textEditAction[name][2] = callBack

    def setDefaultText(self, text):
        self.__defaultText = text
        if self.__contentWrite == False and self.__writent == False:
            self.__textInfos.setText(self.__defaultText)
            self.__updateCursor()
            self.__recalculateCursorPosition(self.__caracterCurseurPosition)

    def getDefaultText(self):
        return self.__defaultText

    def setActionColor(self, name, bgColor, bdColor):
        if name in self.__textEditAction:
            self.__textEditAction[name][0] = bgColor
            self.__textEditAction[name][1] = bdColor

    def updateEvent(self, event):
        action = self.__actualAction
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.__rectangleTextEdit.isContain(Vector2D(event.pos[0], event.pos[1])) == True:
                    action = "pressed"
                    self.__writent = True
                    if self.__contentWrite == False:
                        text = ""
                        self.__contentWrite = True
                        self.__textInfos.setText(text)
                        self.__textInfos.setText(text)
                    else:
                        xi = event.pos[0] - self.__rectangleTextEdit.getPosition().getX() - 5
                        index = self.__textInfos.getCharIndex(self.__textInfos.getArea().x + xi)
                        self.__caracterCurseurPosition = index
                        self.__recalculateCursorPosition(self.__caracterCurseurPosition)
                else:
                    action = "normal"
                    self.__writent = False
                    if len(self.__textInfos.getText()) <= 0:
                        self.__textInfos.setText(self.__defaultText)
                        self.__textInfos.setText(self.__defaultText)
                        self.__contentWrite = False

        elif event.type == MOUSEBUTTONUP and action != "pressed":
            if event.button == 1:
                if self.__rectangleTextEdit.isContain(Vector2D(event.pos[0], event.pos[1])) == True:
                    action = "hover"
                else:
                    action = "normal"
        elif event.type == MOUSEMOTION and action != "pressed":
            if self.__rectangleTextEdit.isContain(Vector2D(event.pos[0], event.pos[1])) == True:
                action = "hover"
            else:
                action = "normal"

        if event.type == KEYDOWN:
            if self.__writent:
                text = self.__textInfos.getText()
                text1 = text[0:self.__caracterCurseurPosition]
                text2 = text[self.__caracterCurseurPosition: len(text)]

                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        if self.__contentWrite == False:
                            text = ""
                            self.__contentWrite = True
                        text1 = text1[:-1]
                        text = text1 + text2
                        self.__caracterCurseurPosition -= 1
                    else:
                        text = self.__defaultText
                        self.__contentWrite = False
                elif event.key == K_LEFT:
                    self.__caracterCurseurPosition -= 1
                    if self.__caracterCurseurPosition < 0:
                        self.__caracterCurseurPosition = 0
                elif event.key == K_RIGHT:
                    self.__caracterCurseurPosition += 1
                    if self.__caracterCurseurPosition > len(self.__textInfos.getText()):
                        self.__caracterCurseurPosition = len(self.__textInfos.getText())
                elif event.key == K_UP:
                    self.__caracterCurseurPosition = len(self.__textInfos.getText())
                elif event.key == K_DOWN:
                    self.__caracterCurseurPosition = 0
                else:
                    if self.__contentWrite == False:
                        text = ""
                        self.__contentWrite = True
                    caracter = event.unicode
                    ascii_lowercase = ' abcdefghijklmnopqrstuvwxyz'
                    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    ascii_letters = ascii_lowercase + ascii_uppercase
                    digits = '0123456789'
                    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~éèàçêôîûâ£$µöïüÿëäù"""
                    printable = digits + ascii_letters + punctuation
                    if caracter in printable:
                        #if len(text1) == len(self.__textInfos.getText()):
                        self.__caracterCurseurPosition += 1
                        text1 += caracter
                        text = text1 + text2

                self.__textInfos.setText(text)
                self.__textInfos.setText(text)
                self.__confineText()
                self.__recalculateCursorPosition(self.__caracterCurseurPosition)

        if action != self.__actualAction:
            self.__actualAction = action
            self.__updateAction()
            if self.__textEditAction[self.__actualAction][2] != None:
                self.__textEditAction[self.__actualAction][2](event)

        if self.__contentWrite == True:
            if self.__textInfos.getColor() != self.__normalTextColor:
                self.__textInfos.setColor(self.__normalTextColor)
                self.__textInfos.setColor(self.__normalTextColor)
        elif self.__textInfos.getColor() != self.__defaultTextColor:
            self.__textInfos.setColor(self.__defaultTextColor)
            self.__textInfos.setColor(self.__defaultTextColor)

    def draw(self, screen):
        self.__rectangleTextEdit.draw(screen)
        self.__textInfos.draw(screen)
        if time.time() % 1 > 0.5 and self.__writent:
            pygame.draw.rect(screen, self.__normalTextColor, self.__cursor)

    def setPosition(self, position):
        self.__rectangleTextEdit.setPosition(position)
        self.__confineText()
        self.__recalculateCursorPosition(self.__caracterCurseurPosition)

    def getPosition(self):
        return self.__rectangleTextEdit.getPosition()

    def setFontName(self, name):
        self.__textInfos.setFontName(name)
        self.__textInfos.setFontName(name)
        self.__confineText()
        self.__recalculateCursorPosition(self.__caracterCurseurPosition)

    def setFontSize(self, size):
        self.__textInfos.setFontSize(size)
        self.__textInfos.setFontSize(size)
        self.__confineText()
        self.__recalculateCursorPosition(self.__caracterCurseurPosition)

    def getFontSize(self):
        return self.__textInfos.getFontSize()

    def getFontName(self):
        return self.__textInfos.getFontName()

    def __updateCursor(self):
        rect = Rect(self.__textInfos.getPosition().getX(), self.__textInfos.getPosition().getY()\
                    , self.__textInfos.getSize().getW(), self.__textInfos.getSize().getH())
        rect.topleft = (self.__rectangleTextEdit.getPosition().getX() + 20, self.__rectangleTextEdit.getPosition().getY() + 20)
        self.__cursor = Rect(rect.topright, (3, rect.height))

    def getSize(self):
        return self.__rectangleTextEdit.getSize()

    def setSize(self, size):
        self.__rectangleTextEdit.setSize(size)
        self.__updateCursor()
        self.__recalculateCursorPosition(self.__caracterCurseurPosition)

    def getStyle(self):
        return self.__textInfos.getStyle()

    def setStyle(self, style):
        self.__textInfos.setStyle(style)
        self.__updateCursor()
        self.__recalculateCursorPosition(self.__caracterCurseurPosition)