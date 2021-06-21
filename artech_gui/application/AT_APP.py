import pygame
from pygame.locals import *
from artech_gui.event.AT_Event import AT_Event
from artech_gui.event.AT_WindowEvent import AT_WindowEvent

class AT_Application(AT_WindowEvent):
    def __init__(self):
        pygame.init()
        self.__width = 640
        self.__height = 480
        self.__title = "Artech GUI"
        self.__flags = RESIZABLE

        self.__screen = pygame.display.set_mode((self.__width, self.__height), self.__flags)
        self.__running = True

        self.__event = AT_Event()

        self.__scene = []
        self.__actual_scene = -1
        self.__event.addEvent(self)

        pygame.display.set_caption(self.__title)

    def __int__(self, title, width, height):
        pygame.display.set_caption(self.__title)
        self.__width = width
        self.__height = height
        __screen = pygame.display.set_mode((self.__width, self.__height), self.__flags)
        self.__event.addEvent(self)

    def addScene(self, scene):
        from artech_gui.application.AT_Scene import AT_Scene
        if isinstance(scene, AT_Scene) or issubclass(scene, AT_Scene):
            self.__scene.append(scene)
            if self.__actual_scene < 0:
                self.__actual_scene = 0

    def removeScene(self, **infos):
        for name, value in infos.items():
            if name.lower() == "index" and value >= 0 and value < len(self.__scene):
                if self.__actual_scene >= value:
                    self.__actual_scene -= 1
                del self.__scene[value]
                return
            elif name.lower() == "memory" and value in self.__scene:
                index = self.__scene.index(value, 0, len(self.__scene - 1))
                if self.__actual_scene >= index:
                    self.__actual_scene -= 1
                self.__scene.remove(value)
            elif name.lower() == "name":
                index = -1
                for scene in self.__scene:
                    index += 1
                    if scene.getName() == value:
                        if self.__actual_scene >= index:
                            self.__actual_scene -= 1
                        self.__scene.remove(scene)
            elif name.lower() == "id":
                index = -1
                for scene in self.__scene:
                    index += 1
                    if scene.getID() == value:
                        if self.__actual_scene >= index:
                            self.__actual_scene -= 1
                        self.__scene.remove(scene)

    def setScene(self, **infos):
        for name, value in infos.items():
            if name.lower() == "index" and value >= 0 and value < len(self.__scene):
                self.__actual_scene = value
            elif name.lower() == "memory" and value in self.__scene:
                self.__actual_scene = self.__scene.index(value, 0, len(self.__scene - 1))
            elif name.lower() == "name":
                index = -1
                for scene in self.__scene:
                    index += 1
                    if scene.getName() == value:
                        self.__actual_scene = index
            elif name.lower() == "id":
                index = -1
                for scene in self.__scene:
                    index += 1
                    if scene.getID() == value:
                        self.__actual_scene = index

    def setMode(self, **flags):
        self.__flags = 0
        add = False
        for key, flag in flags.items():
            if key.lower() == "resize" and flag == True:
                self.__flags ^= RESIZABLE
                add = True
            if key.lower() == "noframe" and flag == True:
                self.__flags ^= NOFRAME
                add = True
            if key.lower() == "fullscreen" and flag == True:
                self.__flags ^= FULLSCREEN
                add = True
        if add:
            self.__updateScreen()

    def run(self):
        while self.__running:
            self.__event.updateEvent()

            self.update(screen=self.__screen)

            self.__screen.fill(Color(0, 162, 232))

            self.draw(self.__screen)
            #pygame.draw.circle(self.__screen, (255, 255, 255), (100, 100), 10)

            pygame.display.update()
        pygame.quit()

    def QUIT(self, event):
        self.__running = False

    def RESIZE(self, event):
        self.__width = event.w
        self.__height = event.h

        self.__updateScreen()

    def __updateScreen(self):
        tmp_screen = self.__screen
        __screen = pygame.display.set_mode((self.__width, self.__height), self.__flags)
        self.__screen.blit(tmp_screen, (0, 0))
        del tmp_screen

    def updateEvent(self, event):
        AT_WindowEvent.updateEvent(self, event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.__running = False

        if self.__actual_scene >= 0 and self.__actual_scene < len(self.__scene):
            self.__scene[self.__actual_scene].updateEvent(event)

    def draw(self, screen):
        if self.__actual_scene >= 0 and self.__actual_scene < len(self.__scene):
            self.__scene[self.__actual_scene].draw(screen)

    def update(self, screen):
        if self.__actual_scene >= 0 and self.__actual_scene < len(self.__scene):
            self.__scene[self.__actual_scene].update(screen)
