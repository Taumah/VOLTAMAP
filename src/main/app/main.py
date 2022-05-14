import pymysql
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition

from homemapview import HomeMapView
from gpshelper import GpsHelper
from src.main.data.connectors import RDSconnector

Window.size = (500, 500)


class NavBar(FakeRectangularElevationBehavior, MDBoxLayout):
    pass

class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    current_lat = 46.227638
    current_lon = 2.213749
    connection = None

    def on_start(self):
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        # Intialise my database
        self.connection = RDSconnector("../../../conf.json")

        GpsHelper().run() # start the gps


MainApp().run()
