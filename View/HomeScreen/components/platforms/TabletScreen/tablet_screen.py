from os import listdir

from kivymd.uix.screen import MDScreen
from os.path import dirname, join
from kivy.lang import Builder

from Components.button import win

Builder.load_file(join(dirname(__file__), "tablet_screen.kv"))


class HomeTabletScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.artist_rv.data = [
            {
                "vc": "OutlineIconButton",
                "icon": "plus-l",
                "theme_icon_color": "Custom",
                "md_bg_color": [0, 0, 0, 1]
            }
        ] + [{"vc": "OutlineImageButton","source": f"assets/images/{image}"} for image in listdir("assets/images")]

        self.ids.art_rv.data = [
            {
                "source": f"assets/images/{image}",
                "name": "Kengo",
                "artist_image": f"assets/images/{image}"
            } for image in listdir("assets/images")]

    def on_enter(self, *args):
        win.pop_bnb()
