"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from View.screens import screens
from Model.database import DataBase
from Components.factory import register_factory
from libs import replace_kivymd_icons
from Components.button import win

replace_kivymd_icons()
register_factory()


class Art(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("imports.kv")
        # This is the screen manager that will contain all the screens of your
        # application.
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.material_style = "M3"
        self.root = MDScreenManager()
        self.database = DataBase()
        spinner = Factory.MDSpinner(line_width=dp(1.5))
        self.dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            on_pre_open=lambda _: setattr(spinner, "active", True),
            on_dismiss=lambda _: setattr(spinner, "active", False)
        )
        self.dialog.add_widget(spinner)
        self.add_screen("login screen", first=True)

    def add_screen(self, name_screen, switch=True, first=False):
        if first:
            self.load_screen(name_screen, switch, first)
            return
        if not self.root.has_screen(name_screen):
            self.dialog.open()
            Clock.schedule_once(lambda _: self.load_screen(name_screen, switch, first), 1)

    def load_screen(self, name_screen, switch, first):
        Builder.load_file(screens[name_screen]["kv"])
        model = screens[name_screen]["model"](self.database)
        controller = screens[name_screen]["controller"](model)

        view = controller.get_view()
        self.root.add_widget(view)
        if switch:
            self.root.current = name_screen
        if not first:
            self.dialog.dismiss()

    def on_start(self):
        win.create_bnb(icons=[
            {
                "icon": "house-f",
                "icon_variant": "house",
                "active": True,
                "on_release": print
            },
            {
                "icon": "image-f",
                "icon_variant": "image",
                "on_release": print
            },
            {
                "icon": "briefcase-simple-f",
                "icon_variant": "briefcase-simple",
                "on_release": print
            },
            {
                "icon": "user-f",
                "icon_variant": "user",
                "on_release": print
            },
        ], icon="squares-four")

    # def on_stop(self):
    #     self.root.children[0].children[0].export_to_png("screenshot.png")


Art().run()
