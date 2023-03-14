from kivymd.uix.screen import MDScreen
from os.path import dirname, join
from kivy.lang import Builder

Builder.load_file(join(dirname(__file__), "tablet_screen.kv"))


class LoginTabletScreenView(MDScreen):
    pass
