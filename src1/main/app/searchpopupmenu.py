from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog

from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi
from kivy.clock import Clock


class SearchPopupMenu(MDDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .7]
        self.events_callback = self.callback #call the callback function below

    # def open(self):
    #     #super.open()
    #     Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)



