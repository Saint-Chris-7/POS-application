
# Keep these two lines until you find what the real solution is

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



class MainTwoapp(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
    MainTwoapp().run()
