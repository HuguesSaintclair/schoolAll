import pygame

class AT_Event():
    __event_queu = []
    __instance = None

    def __init__(self):
        #AT_Event.getInstance()
        pass

    @staticmethod
    def getInstance():
        if AT_Event.__instance == None:
            AT_Event.__instance = AT_Event()
        return AT_Event.__instance

    def updateEvent(self):
        for event in pygame.event.get():
            for evn in AT_Event.__event_queu:
                evn.updateEvent(event)

    def addEvent(self, event):
        AT_Event.__event_queu.append(event)

    def removeEvent(self, event):
        AT_Event.__event_queu.remove(event)

    def clearEvent(self):
        AT_Event.__event_queu.clear()