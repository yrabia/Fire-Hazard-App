from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker


class FarmersMapView(MapView):
    getting_markets_timer = None
    market_tag = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass
        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM DataForMap WHERE latitude > %s AND latitude < %s AND longitude > %s AND longitude < %s " % (
            min_lat, max_lat, min_lon, max_lon)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(markets)
        for market in markets:
            tag = market[3]
            if tag in self.market_tag:
                continue
            else:
                self.add_markets(market)

    def add_markets(self, market):
        # Create the MarketMarker

        lat, lon = market[0], market[1]
        marker = MarketMarker(lat=lat, lon=lon)
        marker.market_data = market

        # Add the MarketMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        tag = market[3]
        self.market_tag.append(tag)
