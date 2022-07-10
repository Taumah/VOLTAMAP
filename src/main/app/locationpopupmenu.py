"""Required Docstring"""
from kivymd.uix.dialog import MDDialog


# pylint: disable=too-many-ancestors
class LocationPopupMenu(MDDialog):
    """Menu on clic"""

    def __init__(self, market_data):
        super().__init__()
        print(market_data)
