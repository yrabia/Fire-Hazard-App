from kivy.app import App

class GpsHelper():
    def run(self):
        # Get a reference to GPS Blinker, then call blink()
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        # Start blinking the GPS blinker
        gps_blinker.blink()
        # Request permissions

        # Configure GPS


