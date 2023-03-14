from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    StringProperty,
    OptionProperty,
    ColorProperty,
    VariableListProperty,
    ListProperty,
    NumericProperty,
    BooleanProperty
)
from kivy.lang import Builder
import kivymd.uix.button.button
from kivy.resources import resource_find
from kivymd.uix.behaviors import RectangularRippleBehavior, MagicBehavior, HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from Components import path
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDIcon
from kivy.core.window import Window as w
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.button import MDIconButton
from kivy.resources import resource_add_path, resource_find
from kivymd import fonts_path, images_path

resource_add_path(fonts_path)
resource_add_path(images_path)
Builder.load_file(str(path / "button" / "button.kv"))


class RoundImageButton(ButtonBehavior, Widget):
    source = StringProperty()


class OutlineIconButton(MDCard, HoverBehavior):
    md_font = StringProperty(resource_find("materialdesignicons-webfont.ttf"))
    font_name = StringProperty()
    theme_icon_color = OptionProperty("Primary", options=kivymd.uix.button.button.theme_text_color_options)
    icon_color = ColorProperty()
    icon = StringProperty()
    font_style = StringProperty("Icons")
    hover_md_bg_color = ColorProperty([1, 1, 1, 1])
    hover_elevate = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_md_bg_color = None

    def on_enter(self):
        if self.hover_elevate:
            self.default_md_bg_color = self.md_bg_color
            self.md_bg_color = self.hover_md_bg_color
            Animation(elevation=8, d=.2).start(self)

    def on_leave(self):
        if self.hover_elevate:
            self.md_bg_color = self.default_md_bg_color
            Animation(elevation=0, d=.2).start(self)


class OutlineImageButton(MDCard):
    source = StringProperty()


class RaisedButton(MDCard):
    text = StringProperty()
    text_color = ColorProperty([1, 1, 1, 1])
    label_padding = VariableListProperty(["25dp", "10dp"], length=2)
    theme_text_color = OptionProperty("Custom", options=kivymd.uix.button.button.theme_text_color_options)


class ListButton(RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()
    icon_bg_color = ColorProperty()


class IconButton(ButtonBehavior, MDIcon):
    pass


class BottomNavigationButton(MDCard, MagicBehavior):
    icon = StringProperty("android")
    icons = ListProperty()
    icon_color = ColorProperty()
    bnb_x = NumericProperty(.5)
    bnb_y = NumericProperty(.03)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon_widget = None
        self.active_icon_data = {}
        self.bind_bnb_size_to_bnb_pos = lambda _, s: setattr(
            self, "pos",
            (
                (self.parent.size[0] * self.bnb_x) - (s[0] * self.bnb_x),
                (self.parent.size[1] * self.bnb_y) - (s[1] * self.bnb_y)
            )
        )
        self.bind(size=self.bind_bnb_size_to_bnb_pos)

    def on_release(self):
        if isinstance(self.children[0], RelativeLayout):
            self.icon_widget = self.children[0]
            anim = Animation(opacity=0, d=.1)
            anim.bind(on_complete=lambda *_: self.remove_widget(self.children[0]))
            anim.start(self.children[0])
            anim2 = Animation(
                width=(dp(48) * len(self.icons)) + ((len(self.icons) - 1) * self.spacing) + dp(40),
                radius=[dp(24)] * 4, padding=[dp(20), 0, dp(20), 0], d=.2)
            anim2.bind(on_complete=self._add_icons)
            anim2.start(self)

    def _add_icons(self, *_):
        for i, data in enumerate(self.icons):
            btn = MDIconButton(
                icon=data["icon"] if data.get("active") else data["icon_variant"],
                on_release=data["on_release"],
                icon_color=[1, 1, 1, 1]
            )
            if data.get("active"):
                btn.dispatch("on_release")
            btn.on_release = lambda instance=btn, icon=data["icon"], index=i: self._icon_on_release(instance, icon,
                                                                                                    index)
            if data.get("active"):
                self.active_icon_data = {"btn": btn, "index": i}
            btn.theme_icon_color = "Custom"
            if font_name := data.get("font_name"):
                btn.font_name = font_name
            self.add_widget(btn)

    def _icon_on_release(self, instance, icon, index):
        if instance is self.active_icon_data["btn"]:
            return
        instance.icon = icon
        self.active_icon_data["btn"].icon = self.icons[self.active_icon_data["index"]]["icon_variant"]
        self.active_icon_data = {"btn": instance, "index": index}


class NoIconException(Exception):
    pass


class win:
    bnb = None
    bind_win_size_to_bnb_pos = None
    state = "pop"
    y = -.1
    x = .5

    @classmethod
    def create_bnb(
            cls,
            icons,
            icon="view-grid-outline",
            icon_color=None,
            md_bg_color=None,
            shadow_color=None,
            parent=None):
        if not icon_color:
            icon_color = [1, 1, 1, 1]
        if isinstance(parent, FloatLayout):
            global w
            w = parent
        cls.bnb = BottomNavigationButton(
            icon=icon,
            icons=icons,
            icon_color=icon_color)
        if md_bg_color:
            cls.bnb.md_bg_color = md_bg_color

        if shadow_color:
            cls.bnb.shadow_color = shadow_color
        bs = cls.bnb.size
        cls.bnb.pos = ((w.size[0] * cls.x) - (bs[0] * cls.x), (w.size[1] * cls.y) - (bs[1] * cls.y))
        cls.bind_win_size_to_bnb_pos = lambda _, s: setattr(
            cls.bnb, "pos",
            (
                (s[0] * cls.x) - (cls.bnb.width * cls.x),
                (s[1] * cls.y) - (cls.bnb.height * cls.y)
            )
        )
        w.bind(size=cls.bind_win_size_to_bnb_pos)
        w.add_widget(cls.bnb)
        return cls.bnb

    @classmethod
    def pop_bnb(cls):
        if cls.state == "push" and cls.bnb.icon_widget:
            cls.bnb.clear_widgets()
            cls.bnb.add_widget(cls.bnb.icon_widget)
            Animation(opacity=1, d=.05).start(cls.bnb.icon_widget)
        cls.y = -.1
        anim = Animation(size=[dp(82), dp(48)], radius=[dp(10)] * 4, d=.2) + Animation(
            y=(w.height * cls.y) - (cls.bnb.height * -cls.y), d=.1)
        anim.bind(on_complete=lambda *_: cls._unbind_win_size_width())
        anim.start(cls.bnb)
        cls.state = "pop"

    @classmethod
    def push_bnb(cls):
        if cls.state == "pop":
            cls._unbind_win_size_width()
            cls._bind_win_size_width()
            cls.y = .03
            anim = Animation(y=(w.height * cls.y) - (cls.bnb.height * cls.y), d=.1)
            anim.bind(on_complete=lambda *_: cls.bnb.wobble())
            anim.start(cls.bnb)
            cls.state = "push"

    @classmethod
    def remove_bnb(cls):
        cls._unbind_win_size_width()
        w.remove_widget(cls.bnb)
        cls.bnb = None

    @classmethod
    def _bind_win_size_width(cls):
        if cls.bnb:
            w.bind(size=cls.bind_win_size_to_bnb_pos)

    @classmethod
    def _unbind_win_size_width(cls):
        if cls.bnb:
            w.unbind(size=cls.bind_win_size_to_bnb_pos)
