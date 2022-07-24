"""Required Docstring"""
# pylint: disable=import-error
from kivy_garden.mapview import MapMarker
from kivy.animation import Animation


class GpsBlinker(MapMarker):
    """Class GpsBlinker"""

    def __init__(self, **kwargs):
        super().__init__()
        self.blink_size = self.default_blink_size
        self.outer_opacity = 1

    def blink(self):
        """
        Function Animation that changes blink size and opacity for animate the blink
        """
        anim = Animation(outer_opacity=0, blink_size=50)
        # When the animation completes, reset the animation, then repeat
        anim.bind(on_complete=self.reset)
        anim.start(self)

    def reset(self, *args):
        """
        Function to reset
        """
        self.blink()
