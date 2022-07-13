"""Required Docstring"""
# pylint: disable=import-error

from locationpopupmenu import LocationPopupMenu
from kivy_garden.mapview import MapMarkerPopup


class MarketMarker(MapMarkerPopup):
    """Place marker on screen"""

    def __init__(self, lat: float, lon: float, **kwargs):
        super().__init__(**kwargs)
        self.lat = lat
        self.lon = lon
        self.source = "./image/custom_marker.png"
        self.texture_size = (25, 25)
        self.market_data = []

    def on_release(self):
        """action off hover"""
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [0.8, 0.25]
        menu.open()

    def get_lat(self):
        """get marker latitude"""
        return self.lat

    def get_lon(self):
        """get marker longitude"""
        return self.lon
