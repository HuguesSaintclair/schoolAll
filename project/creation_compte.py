from artech_gui.application.AT_Scene import AT_Scene
from pygame.locals import *

class CreationCompte(AT_Scene):
    def __init__(self, parent):
        super(CreationCompte, self).__init__(parent)
        self.setName("compte")

    def updateEvent(self, event):
        super(CreationCompte, self).updateEvent(event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.getParent().setScene(name="connexion")

    def draw(self, screen):
        super(CreationCompte, self).draw(screen)