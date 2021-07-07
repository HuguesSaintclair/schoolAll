import speech_recognition as sr
import pyttsx3
import threading
import time
import os
from pocket

r = sr.Recognizer()

class SpeechSay(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      self.__running = True
      self.__commande = ""

      self.__permission = False
   def run(self):
      while self.__running:
          if self.__permission:
             self.SpeakText(self.__commande)
             time.sleep(5)
             self.__permission = False

   def setPermission(self, permission):
       self.__permission = permission

   def close_it(self):
       self.__running = False

   def setCommande(self, commande):
       self.__commande = commande

   def getCommande(self, commande):
       return self.__commande

   def SpeakText(self, command):
       engine = pyttsx3.init()
       engine.say(command)
       engine.runAndWait()

class ListenSay(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      self.__running = True
      self.__text = ""

   def run(self):
      with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source, duration=2)
          while self.__running:
              audio = r.listen(source)
              try:
                  self.__text = r.recognize_sphinx(audio)
                  print("Sphinx thinks you said " + self.__text.lower())
              except sr.UnknownValueError:
                  print("Sphinx could not understand audio")
              except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

   def close_it(self):
       self.__running = False

   def getSay(self):
       text = self.__text
       self.__text = ""
       return text