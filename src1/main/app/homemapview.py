"""Required Docstring"""
# pylint: disable=import-error,broad-except
import sys

from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker
from knnClustering import KnnClustering

class HomeMapView(MapView):
    """Home Map View"""

    getting_markets_timer = None
    market_names = []
    market_ids = []

    def start_getting_markets_in_fov(self):
        """After one second, get the markets in the field of view"""
        try:
            self.getting_markets_timer.cancel()
        except Exception:
            pass
        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def reset_window(self):
        for marker in self.market_names:
            self.remove_widget(marker)

        self.market_names = []
        self.market_ids = []


    def get_markets_in_fov(self, *args):
        """display marker depending on zoom state"""
        # Get reference to main app and the database cursor

        # TODO erase all current markers
        # TODO under 200 elements : display markers
        # TODO under 200 elements : display markers
        # TODO faire un petit ratio afficher plus de cluster quand dezoomer
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT id,latitude,longitude FROM stz_googleAPI WHERE longitude > %s AND longitude < %s AND latitude > %s AND latitude < %s " % (
            min_lon, max_lon, min_lat, max_lat)
        # -3.0435056, 8.3004027, 42.2876432, 51.0482878)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()

        print("nombre de marker", len(markets))
        self.reset_window()

        if len(markets) < 200:
            for market in markets:
                id = market[0]
                if id in self.market_ids:
                    continue
                else:
                    self.add_market(market)
        else:
            # self.reset_window()

            markets = KnnClustering(markets, centroids=12).knn_clustering()
            # marker_layer = ClusteredMarkerLayer(cluster_radius=200)
            for market in markets:
                self.add_market(market)
                # marker_layer.add_marker(market[1], market[2])
            # self.add_layer(marker_layer)
            # self.add_widget()

    def add_market(self, market):
        """create, add and store marker"""
        # Create the MarketMarker
        lat, lon = float(market[1]), float(market[2])
        marker = MarketMarker(lat=lat, lon=lon)
        marker.market_data = market
        # Add the MarketMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        id = market[0]
        self.market_names.append(marker)
        self.market_ids.append(id)
