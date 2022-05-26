from kivy_garden.mapview import MapMarkerPopup, MapMarker
from kivymd.app import MDApp
from kivy.uix.button import Button


class MapViewApp(MDApp):
    def on_start(self):
        marker = MapMarkerPopup(lat=50.6365654, lon=3.0635282, source="./image/custom_marker.png", texture_size=(20, 20))
        marker.add_widget(Button(text="Python button"))
        self.root.add_widget(marker)

        marker2 = MapMarkerPopup(lat=50, lon=3, source="./image/custom_marker.png", texture_size=(20, 20))
        marker.add_widget(Button(text="Python button"))
        self.root.add_widget(marker2)


MapViewApp().run()
