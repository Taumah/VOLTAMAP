"""Required Docstring"""
# pylint: disable=import-error
from kivy.core.window import Window

# Kivy
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

# Class
from gpshelper import GpsHelper
from main.data.connectors.connectors import RDSconnector

#  SQl

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

    def get_connection(self):
        """return connection"""
        return self.connection


MainApp().run()
