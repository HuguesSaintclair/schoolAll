from project.connection import Connection
from project.creation_compte import CreationCompte

from artech_gui.application.AT_APP import AT_Application

class SchoolForAll(AT_Application):
    def __init__(self):
        super(SchoolForAll, self).__init__()

        self.addScene(Connection(self))
        self.addScene(CreationCompte(self))

        self.setScene(name = "connexion")