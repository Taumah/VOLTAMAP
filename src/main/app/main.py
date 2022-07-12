"""Required Docstring"""
# pylint: disable=import-error
from kivy.core.window import Window

# Kivy
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

# Class
from homemapview import HomeMapView
from gpshelper import GpsHelper
from src.main.app.searchpopupmenu import SearchPopupMenu
from src.main.data.connectors.connectors import RDSconnector

#  SQl
import pymysql

Window.size = (500, 500)

# pylint: disable=too-many-ancestors
class NavBar(FakeRectangularElevationBehavior, MDBoxLayout):
    """Bottom navBar"""


class HomeScreen(Screen):
    """Classic Screen Class"""


class MainApp(MDApp):
    """App"""

    def __init__(self, _=None):
        super().__init__()
        self.cursor = None
        self.connection = None
        self.search_menu = None

    def on_start(self):
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        # start the gps
        GpsHelper().run()

        # Intialise my database
        self.connection = RDSconnector("../../../conf.json")
        self.cursor = self.connection.cursor

        self.search_menu = SearchPopupMenu()

    def get_connection(self):
        """return connection"""
        return self.connection


MainApp().run()