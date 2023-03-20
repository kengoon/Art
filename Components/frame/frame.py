from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, VariableListProperty, BooleanProperty, DictProperty, \
    NumericProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.relativelayout import MDRelativeLayout
from Components.button import win
from Components import path
from kivy.lang import Builder
from libs import shorten_text

Builder.load_file(str(path / "frame" / "frame.kv"))


class ImageFrame(RecycleKVIDsDataViewBehavior, BoxLayout, StencilBehavior):
    source = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    name = StringProperty()
    radius = VariableListProperty("20dp", length=4)
    artist_image = StringProperty()
    likes_callback = ObjectProperty(lambda: None)
    comments_callback = ObjectProperty(lambda: None)
    no_comments_likes = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.rv = None

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.rv = rv
        super().refresh_view_attrs(rv, index, data)

    def update_numbers(self, key, value):
        if isinstance(self.parent, RecycleBoxLayout):
            # rv = self.parent.parent
            self.rv.data[self.index][key] = value


class ImageCard(MDBoxLayout, StencilBehavior):
    source = StringProperty()
    name = StringProperty()


class TextFrame(MDRelativeLayout):
    text = StringProperty()
    sayer_name = StringProperty()
    sayer_image = StringProperty()


class FitFrame(MDRelativeLayout):
    frame = StringProperty()
    title = StringProperty()
    text = StringProperty()
    tiny_image = StringProperty()
    text_content_y = NumericProperty("10dp")
    tiny_image_line_color = ColorProperty()
    content_text = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._text_content_y = dp(68)
        if not kwargs.get("tiny_image_line_color"):
            self.tiny_image_line_color = self.theme_cls.primary_color
        if win.state == "push":
            self.text_content_y = self._text_content_y
        win.register_listener(
            pop=lambda: Animation(text_content_y=dp(10), d=.2).start(self),
            push=lambda: Animation(text_content_y=self._text_content_y, d=.2).start(self)
        )

    def shorten_text(self, *args):
        if not self.content_text:
            return
        self.text = shorten_text(
            self.content_text,
            self.ids.content_lbl.width,
            lines=2,
            font_size=self.ids.content_lbl.font_size
        )
