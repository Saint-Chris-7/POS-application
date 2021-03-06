
# Keep these two lines until you find what the real solution is
from cgitb import text
from msilib.schema import Font
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class MyGrid(Widget):
    name= ObjectProperty(None)
    email= ObjectProperty(None)
    
    def btn(self):
        print("Name:", self.name.text, "Email:", self.email.text)
        self.name.text=""
        self.email.text=""


class Myapp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    Myapp().run()

