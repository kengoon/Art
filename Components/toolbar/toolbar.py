from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from Components import path

Builder.load_file(str(path / "toolbar" / "toolbar.kv"))


class BaseToolBar(MDBoxLayout):
    title = StringProperty()
    icon_left = StringProperty()
    button_callback = ObjectProperty(lambda: None)


class ToolBar(BaseToolBar):
    pass


class ImageButtonToolBar(BaseToolBar):
    pass
