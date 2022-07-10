"""Required Docstring"""
# pylint: disable=import-error,broad-except
import sys

from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker


class HomeMapView(MapView):
    """Home Map View"""

    getting_markets_timer = None
    market_names = []

    def start_getting_markets_in_fov(self):
        """After one second, get the markets in the field of view"""
        try:
            self.getting_markets_timer.cancel()
        except Exception:
            print("Error : ")
            sys.exit(1)

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self):
        """display marker depending on zoom state"""
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = (
            "SELECT * FROM stz_googleAPI "
            f"WHERE longitude > {min_lon} AND longitude < {max_lon} AND latitude > {min_lat} "
            f"AND latitude < {max_lat} "
        )
        app.cursor.execute(sql_statement)
        markers = app.cursor.fetchall()
        print(markers)
        print("---------------")
        for marker in markers:
            id_marker = marker[1]
            if id_marker in self.marker_names:
                continue

            self.add_marker(marker)

    def add_marker(self, marker):
        """create, add and store marker"""
        # Create the MarketMarker
        lat, lon = marker[2], marker[3]
        marker = MarketMarker(lat=lat, lon=lon)

        # marker.market_data = market # pas sur

        # Add the MarketMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        id_marker = marker[1]
        self.market_names.append(id_marker)
