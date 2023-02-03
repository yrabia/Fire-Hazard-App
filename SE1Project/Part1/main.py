import sys

from kivymd.app import MDApp
from FarmersMapView import FarmersMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu

from gpshelper import GpsHelper


class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        # Initialize gps
        GpsHelper().run()

        # connect to database
        self.connection = sqlite3.connect("dataformap.db")
        self.cursor = self.connection.cursor()

        # instantiate search popup menus
        self.search_menu = SearchPopupMenu()
