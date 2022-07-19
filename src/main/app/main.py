"""Required Docstring"""
# pylint: disable=import-error

# Kivy
from urllib import parse

from kivy.app import App
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

# Class
from homemapview import HomeMapView
from gpshelper import GpsHelper
from data.connectors.connectors import RDSconnector


Window.size = (500, 500)

# pylint: disable=too-many-ancestors
class NavBar(FakeRectangularElevationBehavior, MDBoxLayout):
    """Bottom navBar"""

class HomeScreen(Screen):
    """Classic Screen Class"""
    #Searchbar functions
    def geocode_get_lat_lon(self, address):
        address = parse.quote(address)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyCVW90LRumD-f_qiTvktpVf0_ZRymE58MA" % \
              address
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest, result):
        print("Success")
        latitude = result["results"][0]["geometry"]["location"]["lat"]
        longitude = result["results"][0]["geometry"]["location"]["lng"]
        mapview = App.get_running_app().root.ids.home_screen.ids.mapview
        mapview.center_on(latitude, longitude)

        #Add exception

    def error(self, urlrequest, result):
        print("Error : ", result)

    def failure(self, urlrequest, result):
        print("Failure : ", result)

    def callback(self, *args):
        address = self.ids.address.text
        self.geocode_get_lat_lon(address)

class MainApp(MDApp):
    """App"""

    def __init__(self, _=None):
        super().__init__()
        self.cursor = None
        self.connection = None
        self.search_menu = None

    def on_start(self):
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        # start the gps
        GpsHelper().run()

        # Initialise the database
        self.connection = RDSconnector("conf.json")
        self.cursor = self.connection.cursor

        #self.search_menu = SearchPopupMenu()

    def get_connection(self):
        """return connection"""
        return self.connection


MainApp().run()
