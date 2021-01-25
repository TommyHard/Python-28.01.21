from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass

class MyApp(App):
    def build(self):

        return Container()      
        
if __name__=="__main__":
    MyApp().run()
