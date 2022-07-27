"""Required Docstring"""
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog


# pylint: disable=too-many-ancestors

class LocationPopupMenu(MDDialog):
    """Menu on clic"""

    def __init__(self, market_data):
        super().__init__()

        # Set up the headers
        headers = "Latitude,Longitude,Nom de la station"
        headers = headers.split(',')

        # Popmenu content
        self.dialog = MDDialog(
            text=str(headers[2]) + " : " + str(market_data[3]) + "\n" +
                 str(headers[0]) + " : " + str(market_data[1]) + "\n" +
                 str(headers[1]) + " : " + str(market_data[2]),

            buttons=
            [
                MDRaisedButton(
                    text="Fermer",
                    on_press=self.close_popup,

                )
            ],
        )
        self.dialog.open()

    def close_popup(self, *args):
        """
        Function to close the popup
        """
        self.dialog.dismiss()