from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker


class HomeMapView(MapView):
    getting_markets_timer = None

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM stationID WHERE x > %s AND x < %s AND y > %s AND y < %s " % \
                        (min_lon, max_lon, min_lat, max_lat)
        app.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(markets)
        for market in markets:
            self.add_market(market)

    def add_market(self, market):
        # Create Marker
        lat, lon = market[1], market[2]
        marker = MarketMarker(lat= lat, long=lon)

        # Add the marker to the map
        self.add_widget(marker)

