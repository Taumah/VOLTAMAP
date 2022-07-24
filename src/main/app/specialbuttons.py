"""Required Docstring"""
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label


class ImageButton(ButtonBehavior, Image):
    """Display a button"""


class LabelButton(ButtonBehavior, Label):
    """Display a label on a button"""
