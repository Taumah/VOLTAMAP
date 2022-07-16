"""Required Docstring"""
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog


# pylint: disable=too-many-ancestors

class LocationPopupMenu(MDDialog):
    """Menu on clic"""

    def __init__(self, market_data):
        super().__init__()

        # Set up the headers
        headers = "id,latitude,longitude"
        headers = headers.split(',')

        #Popmenu content
        self.dialog = MDDialog(
            text = str(headers[0])+ " : " + str(market_data[0]) +"\n"+
            str(headers[1])+ " : " + str(market_data[1]) +"\n"+
            str(headers[2])+ " : " + str(market_data[2]),
            buttons = [MDRaisedButton(text="Fermer")],
        )
        self.dialog.open()