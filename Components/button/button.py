from kivy.clock import Clock
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
    BooleanProperty, ReferenceListProperty
)
from kivy.lang import Builder
import kivymd.uix.button.button
from kivymd.uix.behaviors import RectangularRippleBehavior, MagicBehavior, HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from Components import path
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDIcon
from kivy.core.window import Window as w
from kivy.metrics import dp
from kivymd.uix.button import MDRoundFlatIconButton
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


class HoverRoundIconButton(MDRoundFlatIconButton, HoverBehavior):
    line_color = ColorProperty([0, 0, 0, 0])
    hover_color = ColorProperty(None)
    md_bg_color = ColorProperty([0, 0, 0, 0])
    _transparency = ColorProperty([0, 0, 0, 0])
    icon_variant = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._icon = None

    def on_enter(self):
        self._icon = self.icon
        self.icon = self.icon_variant
        Animation(
            md_bg_color=self.hover_color or self.theme_cls.ripple_color,
            d=.5
        ).start(self)

    def on_leave(self):
        self.icon = self._icon
        Animation(md_bg_color=self._transparency, d=.5).start(self)


class ReactionButton(MDBoxLayout):
    icon = StringProperty()
    icon_color = ColorProperty([1, 1, 1, 1])
    count = StringProperty()
    icon_bg_color = ColorProperty()
    count_color = ColorProperty([1, 1, 1, 1])
    icon_size = NumericProperty("24sp")
    orientation = OptionProperty('vertical', options=('horizontal', 'vertical'))

    def __init__(self, *args, **kwargs):
        self.register_event_type("on_release")
        super().__init__(*args, **kwargs)

    def on_release(self, *args):
        pass


class BottomNavigationButton(MDCard, MagicBehavior):
    icon = StringProperty("android")
    icons = ListProperty()
    icon_color = ColorProperty()
    bnb_x = NumericProperty(.5)
    bnb_y = NumericProperty("10dp")
    expanded = BooleanProperty(False)
    thick_icons = BooleanProperty(False)
    thick_not_selected_color = ColorProperty([.5, .5, .5, .9])
    size_hint = ListProperty([None, None])
    width = NumericProperty("82dp")
    height = NumericProperty("48dp")
    size = ReferenceListProperty(width, height)
    md_bg_color = ColorProperty(None)
    radius = VariableListProperty("10dp")
    elevation = NumericProperty(10)
    shadow_offset = ListProperty([0, -10])
    shadow_softness = NumericProperty(40)

    def __init__(self, *args, **kwargs):
        if not kwargs.get("win"):
            raise AttributeError(f"{self.__name__} must be created from {win} using `win.create_bnb`")
        else:
            del kwargs["win"]
        super().__init__(*args, **kwargs)
        if not self.md_bg_color:
            self.md_bg_color = self.theme_cls.primary_color
        self._spacing = lambda: ((w.width - dp(20)) - (dp(48) * len(self.icons)) - dp(40)) / (len(self.icons) - 1)
        self.icon_widget = RelativeLayout()
        self._inner_icon_widgets = []
        self.icon_widget.add_widget(
            MDIcon(
                icon=self.icon,
                pos_hint={"center": [.5, .5]},
                theme_text_color="Custom",
                text_color=self.icon_color
            )
        )
        Clock.schedule_once(lambda *_: self._create_children())
        self.active_icon_data = {}
        self.bind_bnb_size_to_bnb_pos = lambda _, s: setattr(
            self, "pos", ((self.parent.size[0] * self.bnb_x) - (s[0] * self.bnb_x), self.bnb_y)
        )
        self.bind(icon=self.icon_widget.children[0].setter("icon"))

    def _create_children(self):
        if not self.expanded:
            self.add_widget(self.icon_widget)
        else:
            self.spacing = self._spacing() if w.width < dp(500) else 0
            self.width = w.width - dp(20) if w.width < dp(500) else (dp(48) * len(self.icons)) + dp(40)
            self.radius = [dp(24)] * 4
            self.padding = [dp(20), 0]
            self._add_icons()
        self.bind(size=self.bind_bnb_size_to_bnb_pos)

    def on_release(self):
        if isinstance(self.children[0], RelativeLayout):
            self.icon_widget = self.children[0]
            anim = Animation(opacity=0, d=.1)
            anim.bind(on_complete=lambda *_: self.remove_widget(self.children[0]))
            anim.start(self.children[0])
            anim2 = Animation(
                spacing=self._spacing() if w.width < dp(500) else 0,
                width=w.width - dp(20) if w.width < dp(500) else (dp(48) * len(self.icons)) + dp(40),
                radius=[dp(24)] * 4, padding=[dp(20), 0, dp(20), 0], d=.2)
            anim2.bind(on_complete=self._add_icons)
            anim2.start(self)

    def _add_icons(self, *_):
        if self._inner_icon_widgets:
            for icons in self._inner_icon_widgets:
                self.add_widget(icons)
            return
        for i, data in enumerate(self.icons):
            btn = MDIconButton(
                icon=data["icon"] if data.get("active") or self.thick_icons else data["icon_variant"],
                on_release=data["on_release"],
                icon_color=self.thick_not_selected_color if self.thick_icons and not data.get("active") else [1, 1, 1, 1]
            )
            btn.on_release = lambda instance=btn, icon=data["icon"], index=i: self._icon_on_release(instance, icon,
                                                                                                    index)
            if data.get("active"):
                self.active_icon_data = {"btn": btn, "index": i}
                self._icon_on_release(btn, data["icon"], i)
            btn.theme_icon_color = "Custom"
            if font_name := data.get("font_name"):
                btn.font_name = font_name
            self._inner_icon_widgets.append(btn)
            self.add_widget(btn)

    def _icon_on_release(self, instance, icon, index):
        if instance is self.active_icon_data["btn"]:
            return
        if not self.thick_icons:
            instance.icon = icon
            self.active_icon_data["btn"].icon = self.icons[self.active_icon_data["index"]]["icon_variant"]
        else:
            instance.icon_color = [1, 1, 1, 1]
            self.active_icon_data["btn"].icon_color = self.thick_not_selected_color
        self.active_icon_data = {"btn": instance, "index": index}


class NoIconException(Exception):
    pass


class win:
    bnb = None
    bind_win_size_to_bnb_pos = None
    state = "pop"
    y = dp(10)
    x = .5
    _y = None
    _pop_listeners = []
    _push_listeners = []

    @classmethod
    def create_bnb(
            cls,
            icons,
            icon="view-grid-outline",
            icon_color=None,
            md_bg_color=None,
            shadow_color=None,
            parent=None,
            line_color=None,
            expanded=False,
            thick_icons=False,
            thick_not_selected_color=None
    ):
        if not icon_color:
            icon_color = [1, 1, 1, 1]
        if isinstance(parent, FloatLayout):
            global w
            w = parent
        cls.bnb = BottomNavigationButton(
            icon=icon,
            icons=icons,
            icon_color=icon_color,
            win=True,
            expanded=expanded,
            thick_icons=thick_icons
        )
        if thick_not_selected_color:
            cls.bnb.thick_not_selected_color = thick_not_selected_color
        if md_bg_color:
            cls.bnb.md_bg_color = md_bg_color
        if shadow_color:
            cls.bnb.shadow_color = shadow_color
        if line_color:
            cls.bnb.line_color = line_color
        bs = cls.bnb.size
        cls._y = -cls.y * 5
        cls.bnb.pos = ((w.size[0] * cls.x) - (bs[0] * cls.x), cls._y)
        cls.bind_win_size_to_bnb_pos = lambda _, s: setattr(
            cls.bnb, "pos", ((s[0] * cls.x) - (cls.bnb.width * cls.x), cls._y))
        cls._bind_win_size_width()
        w.add_widget(cls.bnb)
        return cls.bnb

    @classmethod
    def pop_bnb(cls):
        if not cls.state == "push":
            return
        cls.bnb.clear_widgets()
        cls.bnb.add_widget(cls.bnb.icon_widget)
        Animation(opacity=1, d=.05).start(cls.bnb.icon_widget)
        cls._y = -cls.y * 5
        anim = Animation(width=dp(82), padding=[0] * 4, radius=[dp(10)] * 4, d=.2) + Animation(
            y=cls._y, d=.2)
        anim.start(cls.bnb)
        for func in cls._pop_listeners:
            func()
        cls.state = "pop"

    @classmethod
    def push_bnb(cls):
        if not cls.state == "pop":
            return
        cls._y = cls.y
        anim = Animation(y=cls._y, d=.2)
        anim.bind(on_complete=lambda *_: cls.bnb.wobble())
        anim.start(cls.bnb)
        for func in cls._push_listeners:
            func()
        cls.state = "push"

    @classmethod
    def remove_bnb(cls):
        cls._unbind_win_size_width()
        w.remove_widget(cls.bnb)
        cls.bnb = None
        cls.bind_win_size_to_bnb_pos = None

    @classmethod
    def _bind_win_size_width(cls):
        if cls.bnb:
            w.bind(size=cls.bind_win_size_to_bnb_pos)

    @classmethod
    def _unbind_win_size_width(cls):
        if cls.bnb:
            w.unbind(size=cls.bind_win_size_to_bnb_pos)

    @classmethod
    def register_listener(cls, **kwargs):
        if func := kwargs.get("pop"):
            cls._pop_listeners.append(func)
        if func := kwargs.get("push"):
            cls._push_listeners.append(func)
        else:
            raise AttributeError(f"Unknown argument. Argument must be any or both of [pop, push]")
