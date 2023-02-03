from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from gpshelper import GpsHelper


class SearchPopupMenu(MDInputDialog):
    title = 'My Address'
    text_button_ok = 'Go'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        apiKey = "wLJW6ZYj8516o6w7pgccwS_lXozSHgv9_EaR8WDHoIs"
        address = parse.quote(address)
        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext=%s&apiKey=%s" % (address, apiKey)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest, result):
        print("Success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        GpsHelper.gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        GpsHelper.gps_blinker.lat = latitude
        GpsHelper.gps_blinker.lon = longitude
        map = App.get_running_app().root.ids.mapview
        map.center_on(latitude, longitude)

    def error(self, urlrequest, result):
        print("Error")
        print(result)

    def failure(self, urlrequest, result):
        print("Failure")
        print(result)
