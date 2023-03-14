from kivymd.uix.screen import MDScreen
from os.path import dirname, join
from kivy.lang import Builder

Builder.load_file(join(dirname(__file__), "mobile_screen.kv"))


class LoginMobileScreenView(MDScreen):
    pass
