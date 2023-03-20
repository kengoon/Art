# This package is for additional application modules.
from . import patches
from kivy.core.text import LabelBase, Label
from kivymd import icon_definitions
from kivy.resources import resource_add_path, resource_find
from kivymd import fonts_path, images_path
from .icon_def import x_icons
from kivy.metrics import sp

resource_add_path(fonts_path)
resource_add_path(images_path)
icon_font_path = "assets/fonts/icon.ttf"
md_font_path = resource_find("materialdesignicons-webfont.ttf")


def replace_kivymd_icons():
    LabelBase.register(name="Icons", fn_regular=icon_font_path)
    icon_definitions.md_icons.update(x_icons)


def shorten_text(text, lbl_width, lines=1, suffix="... See more", font_size=sp(12)):
    lbl = Label(font_size=font_size)
    new_text = text
    text_width = lbl.get_cached_extents()
    t = 0
    lbl_width *= lines
    if lbl_width <= 0:
        return ""
    while text_width(new_text + suffix + " more")[0] > lbl_width:
        new_text = new_text.split(" ")
        del new_text[-1]
        new_text = " ".join(new_text)
        if text_width(new_text + suffix + " more")[0] == t:
            return ""
        t = text_width(new_text + suffix + " more")[0]
    return new_text + suffix
