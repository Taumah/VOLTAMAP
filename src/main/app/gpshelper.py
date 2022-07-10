"""Required Docstring"""
# pylint: disable=import-error,no-name-in-module,use-a-generator,unused-argument
from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

if platform == "android":
    from android.permissions import Permission, request_permissions
# Configure GPS
if platform == "ios":
    from plyer import gps

if platform == "macosx":
    print("je suis dans mac os")


def open_gps_access_popup():
    """display popup"""
    dialog = MDDialog(
        title="GPS Error",
        text="You need to enable GPS access for the app to function properly",
    )
    dialog.size_hint = [0.8, 0.8]
    dialog.pos_hint = {"center_x": 0.5, "center_y": 0.5}
    dialog.open()


class GpsHelper:
    """Gps Helper Class"""
    has_centered_map = False

    def run(self):
        """On launch method"""
        print("Je suis sur la plateform", platform)

        # Get a reference to GpsBlinker, then call blink()
        gps_blinker = App.get_running_app().root.ids.home_screen.ids.mapview.ids.blinker
        # Start blinking the GpsBlinker
        gps_blinker.blink()

        # Request permissions on Android

        def callback(permission, results):
            if all(results):
                print("Got all permissions")

                gps.configure(
                    on_location=self.update_blinker_position,
                    on_status=self.on_auth_status,
                )
                gps.start(minTime=1000, minDistance=0)
            else:
                print("Did not get all permissions")
                print("Current permission: ", permission)

        request_permissions(
            [Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION],
            callback,
        )

        gps.configure(
            on_location=self.update_blinker_position, on_status=self.on_auth_status
        )
        gps.start(minTime=1000, minDistance=0)

    def update_blinker_position(self, *args, **kwargs):
        """update blinker position"""
        my_lat = kwargs["lat"]
        my_lon = kwargs["lon"]
        print("GPS POSITION", my_lat, my_lon)
        # Update GpsBlinker position
        gps_blinker = App.get_running_app().root.ids.home_screen.ids.mapview.ids.blinker
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon

        # Center map on gps
        if not self.has_centered_map:
            map_view = App.get_running_app().root.ids.home_screen.ids.mapview
            map_view.center_on(my_lat, my_lon)
            self.has_centered_map = True

    def on_auth_status(self, general_status, status_message):
        """popup when authenticated"""
        if general_status == "provider-enabled":
            pass
        else:
            open_gps_access_popup()
