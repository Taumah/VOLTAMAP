from kivymd.uix.dialog import MDDialog


class LocationPopupMenu(MDDialog):
    def __init__(self, market_data):
        super().__init__()
        print(market_data)