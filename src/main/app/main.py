"""Required Docstring"""
# pylint: disable=import-error
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

# Kivy
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

# Class
from homemapview import HomeMapView
from gpshelper import GpsHelper
from searchpopupmenu import SearchPopupMenu
from data.connectors.connectors import RDSconnector

#  SQl
#import pymysql

Window.size = (500, 500)

kv = '''
ScreenManager:
    HomeScreen:

<HomeScreen>:
    MDBoxLayout:
        orientation : "vertical"
        md_bg_color: 1, 1, 1, 1
        MDBoxLayout:
            adaptive_height: True
            padding : "20dp"
            MDTextFieldRound:
                id : address
                hint_text: 'Search EV charging station'
                pos_hint:{'center_x': 1,'center_y': 0.5}
                size_hint: 1, None

                color_active: 0, 1, 0, 1
                #color_mode: 'custom'
                #line_color: 0, 1, 0, 1

            MDIconButton:
                icon: 'map-search'
                on_press: app.show_popup(title.text, body.text)


        HomeMapView:
            pos_hint: {"top": .795, "left": 1}
            size_hint: 1, .695
            id: mapview

        # Bottom NavBar
        NavBar:
            id: navbar
            size_hint: .85, .1
            pos_hint: {"center_x": .5, "center_y": .1}
            elevation: 10
            md_bg_color: 1,1,1,1
            radius: [16]
            width: self.width

            MDGridLayout:
                cols: 4
                size_hint_x: .9
                spacing : 8
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                AnchorLayout:
                    MDIconButton:
                        id: nav_icon1
                        icon: "map"
                        ripple_scale: 0
                        user_font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                AnchorLayout:
                    MDIconButton:
                        id: nav_icon2
                        icon: "transit-connection-variant"
                        ripple_scale: 0
                        user_font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                AnchorLayout:
                    MDIconButton:
                        id: nav_icon3
                        icon: "account-group"
                        ripple_scale: 0
                        user_font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                AnchorLayout:
                    MDIconButton:
                        id: nav_icon4
                        icon: "account"
                        ripple_scale: 0
                        user_font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
'''

# pylint: disable=too-many-ancestors
class NavBar(FakeRectangularElevationBehavior, MDBoxLayout):
    """Bottom navBar"""

class HomeScreen(Screen):
    """Classic Screen Class"""



# class MemoryManagementSystem(ScreenManager):
#     def __init__(self, **kwargs):
#         super(MemoryManagementSystem, self).__init__(**kwargs)
#         print(self.manager.get_screen('homescreen').ids.address.text)
#     def transit_scene(self, *args):
#         self.current = "homescreen"
#
#     def on_enter(self, *largs):
#         address = StringProperty()
#         homescreen = self.manager.get_screen('homescreen')
#         self.address = homescreen.ids.address.text



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

        # Intialise my database
        self.connection = RDSconnector("conf.json")
        self.cursor = self.connection.cursor

        self.search_menu = SearchPopupMenu()

    def get_connection(self):
        """return connection"""
        return self.connection


MainApp().run()
