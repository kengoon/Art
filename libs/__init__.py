# This package is for additional application modules.
from . import patches
from kivy.core.text import LabelBase
from kivymd import icon_definitions
from kivy.resources import resource_add_path, resource_find
from kivymd import fonts_path, images_path
from .icon_def import x_icons

resource_add_path(fonts_path)
resource_add_path(images_path)
icon_font_path = "assets/fonts/icon.ttf"
md_font_path = resource_find("materialdesignicons-webfont.ttf")


def replace_kivymd_icons():
    LabelBase.register(name="Icons", fn_regular=icon_font_path)
    icon_definitions.md_icons.update(x_icons)
