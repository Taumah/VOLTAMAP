from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker
from knnClustering import KnnClustering


class HomeMapView(MapView):
    getting_markets_timer = None
    market_names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        '''


        '''
        # Get reference to main app and the database cursor
        self.market_names = []
        # TODO erase all current markers
        # TODO under 200 elements : display markers
        # TODO under 200 elements : display markers
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT id,latitude,longitude FROM stz_googleAPI WHERE longitude > %s AND longitude < %s AND latitude > %s AND latitude < %s " % (
            min_lon, max_lon, min_lat, max_lat)
            # -3.0435056, 8.3004027, 42.2876432, 51.0482878)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(len(markets))
        markets = KnnClustering(markets, centroids=4).knn_clustering()
        # print("---------------")
        for market in markets:
            id = market[0]
            if id in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        # Create the MarketMarker
        lat, lon = market[1], market[2]
        marker = MarketMarker(lat=lat, lon=lon)

        # marker.market_data = market # pas sur

        # Add the MarketMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        id = market[0]
        self.market_names.append(id)
