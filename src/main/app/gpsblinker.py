"""Required Docstring"""
# pylint: disable=import-error
from kivy_garden.mapview import MapMarker
from kivy.animation import Animation


class GpsBlinker(MapMarker):
    """Class GpsBlinker"""

    def __init__(self):
        self.blink_size = None
        self.outer_opacity = None

    def blink(self):
        """on hover action"""
        # Animation that changes the blink size and opacity
        anim = Animation(outer_opacity=0, blink_size=50)
        # When the animation completes, reset the animation, then repeat
        anim.bind(on_complete=self.reset)
        anim.start(self)

    def reset(self,  _):
        """off hover action"""
        self.outer_opacity = 1
        self.blink_size = self.default_blink_size
        self.blink()
