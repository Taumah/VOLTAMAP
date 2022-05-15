from kivy_garden.mapview import MapMarkerPopup, MapMarker, MapView
from kivy.properties import NumericProperty


class MarketMarker(MapMarkerPopup):
    source = "image/custom_marker.png"
    size_hint = (150,150)

    def on_release(self):
        pass
