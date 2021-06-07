from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

class LoginScreen(MDApp):
    def build(self):
        return Builder.load_file("loginScreen.kv")

class MainApp(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("login.kv")

    def logger(self):
        if self.root.ids.user.text == "charlie" and self.root.ids.password.text == "junior":
            self.root.ids.error.text = "bien venu Mr charlie"
            self.root.ids.error.color = [0, 0, 1]
        else:
            self.root.ids.error.text = "erreur logging ou password erroner"
            self.root.ids.error.color = [1, 0, 0]

    def clear(self):
        self.root.ids.error.text = ""
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

if __name__ == "__main__":
    MainApp().run()