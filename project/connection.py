from artech_gui.application.AT_Scene import AT_Scene
from pygame.locals import *

from artech_gui.widget.AT_Text import AT_Text
from artech_gui.maths.AT_Coord import *
from artech_gui.widget.AT_Button import AT_Button
from artech_gui.widget.AT_TextEdit import AT_TextEdit

class Connection(AT_Scene):
    def __init__(self, parent):
        super(Connection, self).__init__(parent)
        self.setName("connexion")
        self.setBackground(color=Color(55, 196, 255))

        self.textEdit = AT_TextEdit()
        self.textEdit.setPosition(Vector2D(100, 100))
        self.textEdit.setAction("textChange", self.textChange)
        self.textEdit.setFontSize(50)

        self.test = self.textEdit

    def updateEvent(self, event):
        super(Connection, self).updateEvent(event)
        self.test.updateEvent(event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
                #self.getParent().setScene(name = "compte")

    def draw(self, screen):
        super(Connection, self).draw(screen)
        self.test.draw(screen)

    def textChange(self, event, lastText, newText):
        print("click Me button")