from pygame.locals import  *

class AT_WindowEvent():
    def __init__(self):
        pass

    def updateEvent(self, event):
        if event.type == QUIT:
            self.QUIT(event)
        if event.type == VIDEORESIZE:
            self.RESIZE(event)

    def QUIT(self, event):
        pass

    def RESIZE(self, event):
        pass