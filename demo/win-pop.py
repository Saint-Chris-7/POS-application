import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup



class Widgets(Widget):
    def btn(self):
        show_popup()
    
class P(FloatLayout):
    pass

class PopApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show= P()
    popupWindow= Popup(title="popup window", content=show, size_hint=(None,None),size=(400,400))
    popupWindow.open()

    

if __name__=="__main__":
    PopApp().run()

