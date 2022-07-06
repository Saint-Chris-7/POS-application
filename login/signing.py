from kivy.app import App
import os
from kivy.uix.boxlayout import BoxLayout
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class SigningWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def validate_user(self):
        user = self.ids.username_field #self.ids. has the ids that are defined in the kv file.
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname= user.text
        pwd = pwd.text

        if uname == "" or pwd == "":
            info.text = "[color=#FF0000]username and or password is required[/color]"
        else:
            if uname == "admin" and pwd == "admin":
                info.text = "[color=#00FF00] logged in successfully [/color]"
            else:
                info.text = "[color=#FF0000]Invalid username or password is required[/color]"
class SigningApp(App):
    def build(self):
        return SigningWindow()

if __name__=="__main__":
    SigningApp().run()