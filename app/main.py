from kivy.app import App
from kivy.uix.button import Button

class CBIR(App):
    def build(self):
        return Button(text="Hello World")

CBIR().run()