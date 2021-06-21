from artech_gui.application.AT_Scene import AT_Scene
from pygame.locals import *

from artech_gui.widget.AT_Text import AT_Text
from artech_gui.maths.AT_Coord import *
from artech_gui.widget.AT_Button import AT_Button

class Connection(AT_Scene):
    def __init__(self, parent):
        super(Connection, self).__init__(parent)
        self.setName("connexion")
        self.setBackground(color=Color(255, 255, 255))

        self.bouton = AT_Button()
        self.bouton.setPosition(Vector2D(100, 100))
        self.bouton.setAction("pressed", self.clickMe)
        self.bouton.setFontSize(50)

    def updateEvent(self, event):
        super(Connection, self).updateEvent(event)
        self.bouton.updateEvent(event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.getParent().setScene(name = "compte")

    def draw(self, screen):
        super(Connection, self).draw(screen)
        self.bouton.draw(screen)

    def clickMe(self, event):
        print("click Me button")