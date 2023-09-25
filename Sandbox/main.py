# The reason for this is so I can test out ideas...

import kivy
from kivy.app import App
from kivy.uix.label import Label

class ForestFox(App):
    def build(self):
        return Label(text = "Hello there", font_size = '24dp')
    

if __name__ == "__main__":
    ForestFox().run()