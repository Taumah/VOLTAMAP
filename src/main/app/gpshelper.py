"""Required Docstring"""
# pylint: disable=import-error,no-name-in-module,use-a-generator,unused-argument
from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog


class GpsHelper:
    """Gps Helper Class"""

    has_centered_map = False

    def run(self):
        """
        Function to run the gps
        """
        print("I m on the plateform : ", platform)
        # Get a reference to GpsBlinker, then call blink()
        gps_blinker = App.get_running_app().root.ids.home_screen.ids.mapview.ids.blinker
        # Start blinking the GpsBlinker
        gps_blinker.blink()

        # Request permissions on Android
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                    from plyer import gps
                    gps.configure(on_location=self.update_blinker_position,
                                  on_status=self.on_auth_status)
                    gps.start(minTime=1000, minDistance=0)
                else:
                    print("Did not get all permissions")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

        # Configure GPS
        if platform == 'ios':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)
        if platform == 'macosx':
            print("je suis dans mac os")

    def update_blinker_position(self, *args, **kwargs):
        """update blinker position"""
        my_lat = kwargs['lat']
        my_lon = kwargs['lon']
        print("GPS POSITION", my_lat, my_lon)
        # Update GpsBlinker position
        gps_blinker = App.get_running_app().root.ids.home_screen.ids.mapview.ids.blinker
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon

        # Center map on gps
        if not self.has_centered_map:
            map = App.get_running_app().root.ids.home_screen.ids.mapview
            map.center_on(my_lat, my_lon)
            self.has_centered_map = True

    def on_auth_status(self, general_status, status_message):
        """popup when authenticated"""
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        """
        Open the popup to allowing worry about a malfunction
        """
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()
