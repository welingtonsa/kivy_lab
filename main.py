# arquivo main.py
# importes necessarios para o algoritimo
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy


# LogimScreem ##########################################
class HomeScreen(Screen):
    pass

# SettingsScreen #######################################
class TextScreen(Screen):
    pass

# Textview Spans Screen ################################
class TextViewSpansScreen(Screen):
    pass

# Insert a file into the language builder and return ##
# thr root widget(if difined) of the kv file. 
GUI = Builder.load_file("main.kv")
# Classe principal #####################################
class AplicativoApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        #print(self.root.ids)
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
AplicativoApp().run()