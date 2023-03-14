from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.color_definitions import colors

from Components import path
from kivy.lang import Builder

Builder.load_file(str(path / "frame" / "frame.kv"))


class ImageFrame(RecycleKVIDsDataViewBehavior, BoxLayout, StencilBehavior):
    source = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    name = StringProperty()
    likes_callback = ObjectProperty(lambda: None)
    comments_callback = ObjectProperty(lambda: None)

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
    date = StringProperty()


class TextFrame(MDRelativeLayout):
    text = StringProperty()
    sayer_name = StringProperty()
    sayer_image = StringProperty()

