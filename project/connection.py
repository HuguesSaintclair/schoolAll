import pygame.time

from artech_gui.application.AT_Scene import AT_Scene
from pygame.locals import *

from artech_gui.widget.AT_Text import AT_Text
from artech_gui.maths.AT_Coord import *
from artech_gui.widget.AT_Button import AT_Button
from artech_gui.widget.AT_TextBox import AT_TextBox
from artech_gui.geometrie.AT_Rectange import AT_Rectangle
from artech_gui.maths.AT_Coord import Vector2D, Size2D

from project.speecher import *

class Connection(AT_Scene):
    def __init__(self, parent):
        super(Connection, self).__init__(parent)
        self.setName("connexion")
        self.setBackground(color=Color(55, 196, 255))

        self.__pseudo = AT_TextBox()
        self.__pseudo.setDefaultText("Pseudo")
        self.__password = AT_TextBox()
        self.__password.setDefaultText("Password")
        self.__password.setStyle("password")
        self.__connexion = AT_Button()
        self.__connexion.setText("Connexion")
        self.__connexion.setSize(Size2D(self.__connexion.getSize().getW(), 40))

        self.__creatAccount = AT_Button()
        self.__creatAccount.setText("Création compte")
        self.__creatAccount.setSize(Size2D(self.__creatAccount.getSize().getW(), 40))

        self.__card = AT_Rectangle()
        self.__cardOmbre = AT_Rectangle()
        self.__card.setSize(Size2D(400, 300))
        self.__cardOmbre.setSize(Size2D(400, 300))
        self.__card.setBorderRadius(5)
        self.__cardOmbre.setBorderRadius(5)
        self.__cardOmbre.setBgColor(Color(200, 200, 200))

        self.__responsive(None)
        self.getParent().addSignal("responsive", self.__responsive)

        self.__run = False

        self.__curentTime = pygame.time.get_ticks()
        self.__previousTime = self.__curentTime

        self.__say = SpeechSay()
        self.__say.start()
        self.__listen = ListenSay()
        self.__listen.start()

    def __responsive(self, event):
        x = (self.getParent().getSize().getW() - self.__card.getSize().getW()) / 2
        y = (self.getParent().getSize().getH() - self.__card.getSize().getH()) / 2
        self.__card.setPosition(Vector2D(x, y))
        self.__cardOmbre.setPosition(Vector2D(x + 3, y + 3))

        x1 = x + (self.__card.getSize().getW() - self.__password.getSize().getW()) / 2
        y1 = y + 50
        y2 = y1 + 10 + self.__password.getSize().getH()

        self.__pseudo.setPosition(Vector2D(x1, y1))
        self.__password.setPosition(Vector2D(x1, y2))

        x2 = x + (self.__card.getSize().getW() - self.__connexion.getSize().getW()) / 2
        y3 = y2 + 50 + self.__password.getSize().getH()
        self.__connexion.setPosition(Vector2D(x2, y3))

        self.__creatAccount.setPosition(Vector2D(x2, y3 + self.__connexion.getSize().getH() + 10))

    def updateEvent(self, event):
        super(Connection, self).updateEvent(event)
        self.__pseudo.updateEvent(event)
        self.__password.updateEvent(event)
        self.__connexion.updateEvent(event)
        self.__creatAccount.updateEvent(event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
                #self.getParent().setScene(name = "compte")

    def draw(self, screen):
        super(Connection, self).draw(screen)
        self.__cardOmbre.draw(screen)
        self.__card.draw(screen)
        self.__pseudo.draw(screen)
        self.__password.draw(screen)
        self.__connexion.draw(screen)
        self.__creatAccount.draw(screen)

        if self.__run == False:
            self.__run = True

    def textChange(self, event, lastText, newText):
        print("click Me button")

    def update(self, screen):
        if self.__run:
            text = self.__listen.getSay()

            if text != "":
                self.__say.setCommande("you say {}".format(text))
                self.__say.setPermission(True)
            else:
                self.__say.setCommande("say connection to connect you")
                self.__say.setPermission(True)


    def finish(self):
        self.__say.join()
        self.__listen.join()