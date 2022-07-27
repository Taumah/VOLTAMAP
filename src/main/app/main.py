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

    def geocode_get_lat_lon(self, address):
        """
        function to get
        """
        address = parse.quote(address)
        url = "https://geocode.search.hereapi.com/v1/geocode?q=%s&apiKey=3elYArDHTylMIMjwzbR2EoPdNj7nvyn7EtFYIFr9o_4" % \
              address
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest: None, result):
        """
        Sucess function to retrieve longitude, latitude and changes the location of the map
        """
        print("Success")
        try:
            latitude = result["items"][0]["position"]["lat"]
            longitude = result["items"][0]["position"]["lng"]
            mapview = App.get_running_app().root.ids.home_screen.ids.mapview
            mapview.center_on(latitude, longitude)
            App.get_running_app().root.ids.home_screen.ids.mapview.zoom = 15

        except Exception as error:
            print("Error", error)

    def error(self, urlrequest: None, result):
        """
        Function error : print error if this occurs
        """
        print("Error : ", result)

    def failure(self, urlrequest: None, result):
        """
        Function failure : print failure if this occurs
        """
        print("Failure : ", result)

    def callback(self, *args):
        """
        Function callback : recuperate the text of the button on_press
        """
        address = self.ids.address.text
        self.geocode_get_lat_lon(address)

    def check(self):
        text = self.ids.address.text
        print("You have enter : ", text)


class MainApp(MDApp):
    """App"""

    def __init__(self, _=None):
        super().__init__()
        self.cursor = None
        self.connection = None
        self.search_menu = None

    def on_start(self):
        """
        Call of all functions at the start of the project
        """
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        # start the gps
        GpsHelper().run()

        # Initialise the database
        self.connection = RDSconnector("conf.json")
        self.cursor = self.connection.cursor

        # self.search_menu = SearchPopupMenu()

    def get_connection(self):
        """return connection"""
        return self.connection


MainApp().run() # Lunch the project
