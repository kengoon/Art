from os import listdir

from kivymd.uix.screen import MDScreen
from os.path import dirname, join
from kivy.lang import Builder

Builder.load_file(join(dirname(__file__), "mobile_screen.kv"))


class ArtMobileScreenView(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.rv.data = [
            {
                "frame": f"assets/images/{image}",
                "title": "Alisha Keys",
                "tiny_image": f"assets/images/{image}",
                "content_text":
                    "It has been a horrible day dancing and singing with so many stupid clowns. This is kinda fun right"
            } for image in listdir("assets/images")]
