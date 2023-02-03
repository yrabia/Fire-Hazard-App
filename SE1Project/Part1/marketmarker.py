from kivy.garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class MarketMarker(MapMarkerPopup):
    market_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .35]
        menu.open()
