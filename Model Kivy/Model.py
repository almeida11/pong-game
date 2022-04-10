from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout 
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'height', 400)
Config.set('graphics', 'width', 650)

from GamePanel import GamePanel

class HelpLabel(Label):
    def __init__(self, **kwargs):
        super(HelpLabel, self).__init__(**kwargs)
        self.text = "W|S->left paddle  UP|DOWN->right paddle  ; Score point by making ball touch opposite wall"

    def setup(self):
        self.size_hint = (1,0.05)
        self.pos_hint = {'y':0.95, 'center_x':0.5}

class MainLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.widget1 = HelpLabel()
        self.widget2 = GamePanel()
        self.add_widget(self.widget1)
        self.add_widget(self.widget2)
        self.widget1.setup()
        self.widget2.setup()

class PongApp(App):
    def build(self):
        return MainLayout()

if __name__=='__main__':
    PongApp().run()