from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy_garden.mapview.clustered_marker_layer import ClusteredMarkerLayer

from marketmarker import MarketMarker


class HomeMapView(MapView):
    getting_markets_timer = None
    market_names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_ev, 1)

    def get_ev(self, *args):
        app = App.get_running_app()
        sql_statement = "SELECT * FROM stz_googleAPI"
        app.cursor.execute(sql_statement)
        ev = app.cursor.fetchall()

        #print(ev)
        for ev_station in ev:
            print(ev_station)  # crash
            self.add_ev_station(ev_station)

        # for ev_station in ev:
        #     id = ev_station[1]
        #     if id in self.market_names:
        #         continue
        #     else:
        #         self.add_ev_station(ev_station)

    def add_ev_station(self, ev):
        lat, lon = ev[2], ev[3]

        ev_station = ClusteredMarkerLayer(cluster_radius=200)

        self.ids.mapview.add_layer(ev_station)

        self.add_marker(lon, lat)

        # id = ev_station[1]
        # self.market_names.append(id)
