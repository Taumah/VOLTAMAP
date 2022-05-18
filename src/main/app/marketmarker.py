from kivy_garden.mapview import MapMarkerPopup
from kivy.properties import NumericProperty


class MarketMarker(MapMarkerPopup):
    lat = float
    lon = float

    def __init__(self, lat, lon, **kwargs):
        super().__init__(**kwargs)
        self.lat = lat
        self.lon = lon
        self.source = "./image/custom_marker.png"
        self.texture_size = (25, 25)

    def on_release(self):
        pass
