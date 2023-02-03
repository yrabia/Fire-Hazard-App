import os
import sys

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from Part1.main import MainApp
from Part1.maintest import TestApp
from kivy.app import App

Window.size = (500, 700)
# original window size: 300,500

navigation_helper = """

#:include main.kv
#:include test.kv
#:import MainApp Part1.main.MainApp
#:import TestApp Part1.maintest.TestApp
NavigationLayout:
    ScreenManager:
        id:screen_manager
        Screen:
            name: "main"
            BoxLayout:
                orientation:'vertical'
                MDToolbar:
                    title: "Menu"
                    elevation: 10
                    left_action_items:[['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                Widget:
                
    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:
            orientation: 'vertical'
                
            Button:
                text:"Map of California"
                on_release:
                    MainApp().run()
                        
            Button:
                text:"View Disaster Info"
                on_release:
                    TestApp().run()
            

"""


class DisasterAppApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(navigation_helper)
        return screen

    def start_over(self):
        os.execl(sys.executable, os.path.abspath('ui.py'), *sys.argv)


DisasterAppApp().run()
