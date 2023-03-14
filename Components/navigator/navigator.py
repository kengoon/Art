from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty, ListProperty, DictProperty, OptionProperty, ObjectProperty
from kivy.lang import Builder
from kivymd.uix.card import MDSeparator
from Components import path
from os import environ
from kivy.animation import Animation

Builder.load_file(str(path / "navigator" / "navigator.kv"))


class BoxIconButton(MDBoxLayout):
    icon = StringProperty()
    icon_pos_hint = DictProperty({"center_x": .5})
    icon_color = ListProperty([0, 0, 0, 1])
    disabled_icon = BooleanProperty(False)
    button_callback = ObjectProperty(lambda: None)

    def ping_parent(self, button_instance):
        self.parent.parent.update_active_icon(button_instance)


class Navigator(MDBoxLayout):
    icons = ListProperty()
    '''
    list of dictionaries containing the ``BoxIconButton`` properties and values
    '''
    separator_position = OptionProperty(None, options=["bottom", "top"])

    active_color = ListProperty()

    disable_active_color = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.active_color and not self.disable_active_color:
            self.active_color = self.theme_cls.primary_color
        Clock.schedule_once(self.add_icons)
        Clock.schedule_once(self.add_separator)

    def add_icons(self, *_):
        for icon in self.icons:
            self.ids.nav.add_widget(BoxIconButton(**icon))
        if not self.disable_active_color:
            self.ids.nav.children[-1].icon_widget.icon_color = self.active_color or [0, 0, 0, 1]
            if environ.get("phosphor"):
                self.ids.nav.children[-1].icon_widget.icon = \
                    self.ids.nav.children[-1].icon_widget.icon.rsplit("-", 1)[0] + "-f"

    def add_separator(self, *_):
        if self.separator_position == "bottom":
            self.add_widget(MDSeparator())
        elif self.separator_position == "top":
            self.add_widget(MDSeparator(), index=1)

    def update_active_icon(self, button_instance):
        if self.disable_active_color:
            return
        icon_parent = self.ids.nav.children
        for child in icon_parent:
            if child.icon_widget == button_instance:
                Animation(icon_color=self.active_color or [0, 0, 0, 1], d=.3).start(button_instance)
                if environ.get("phosphor"):
                    button_instance.icon = button_instance.icon.rsplit("-", 1)[0] + "-f"
                continue
            child.icon_widget.icon_color = [0, 0, 0, 1]
            if environ.get("phosphor"):
                child.icon_widget.icon = child.icon_widget.icon.rsplit("-", 1)[0] + "-l"


if __name__ == "__main__":
    from kivymd.app import MDApp
    from textwrap import dedent


    class TestApp(MDApp):
        def build(self):
            return Builder.load_string(dedent(
                '''
                RelativeLayout:
                    on_touch_down: print(self.children)
                    Navigator:
                        icons: [{'icon': 'android'}]*5
                ''')
            )

        # def on_start(self):
        #     self.root.add_widget(Navigator(icons=[{"icon": "android"}]*5))


    TestApp().run()
