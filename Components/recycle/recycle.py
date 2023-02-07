from kivy.clock import Clock
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from Components import path

Builder.load_file(str(path / "recycle" / "recycle.kv"))


class RecycleContent(RecycleKVIDsDataViewBehavior, ButtonBehavior, MDBoxLayout):
    profile_image = StringProperty("user-circle-d")
    post_text = StringProperty()
    post_image = StringProperty()
    poster_name = StringProperty()
    poster_username = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = None

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        try:
            if rv.data[index]["_size"][1] != self.ids.b.height:
                rv.data[index] = {**rv.data[index], "_size": [0, self.ids.b.height]}
        except KeyError:
            rv.data[index] = {**rv.data[index], "_size": [0, self.ids.b.height]}
        return super().refresh_view_attrs(rv, index, data)


class RecycleTask(RecycleKVIDsDataViewBehavior, ButtonBehavior, MDBoxLayout):
    profile_image = StringProperty("user-circle-d")
    post_text = StringProperty()
    post_image = StringProperty()
    poster_name = StringProperty()
    poster_username = StringProperty()


class RecycleBeggar(RecycleKVIDsDataViewBehavior, ButtonBehavior, MDBoxLayout):
    profile_image = StringProperty("user-circle-d")
    profile_name = StringProperty("Akubue Kenechukwu")
    tag = StringProperty("Beggar")
