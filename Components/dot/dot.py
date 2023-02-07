from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.theming import ThemableBehavior
from kivy.properties import ListProperty, NumericProperty, ColorProperty, BooleanProperty
from kivy.lang import Builder
from Components import path

Builder.load_file(str(path / "dot" / "dot.kv"))


class Dot(ThemableBehavior, Widget):
    current_index = NumericProperty(0)
    color_round_not_active = ListProperty()
    bg_color = ColorProperty(None)
    active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.color_round_not_active:
            self.color_round_not_active = get_color_from_hex("#757575")
