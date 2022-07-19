from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

KV = '''
<Content>
    id: content
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        id: city
        hint_text: "City"

    MDTextField:
        hint_text: "Street"


MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_confirmation_dialog()
'''


class Content(BoxLayout):
    pass


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Fermer",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press= self.close_popup,
                    ),
                    MDFlatButton(
                        text="Valider",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= self.printer,

                    ),
                ],
            )
        self.dialog.open()

    def close_popup(self, *args):
        self.dialog.dismiss()

    def printer(self, *args):
        print(self.dialog.content_cls.ids.city.text)


Example().run()