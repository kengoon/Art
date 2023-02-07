from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, OptionProperty, NumericProperty
from kivy.lang import Builder
from Components import path
from Components.card import Card
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file(str(path / "textfield" / "textfield.kv"))


class TextField(MDCard):
    text_validate_callback = ObjectProperty(lambda: None)
    text = StringProperty()
    multiline = BooleanProperty(False)
    password = BooleanProperty(False)
    hint_text = StringProperty()
    write_tab = BooleanProperty(False)
    icon = StringProperty()
    focus = BooleanProperty(False)
    font_size = NumericProperty('15sp')
    button_icon = StringProperty()
    button_callback = ObjectProperty(lambda _: None)
    input_filter = ObjectProperty(None, allownone=True)
    input_type = OptionProperty('null', options=('null', 'text', 'number',
                                                 'url', 'mail', 'datetime',
                                                 'tel', 'address'))


class TagTextField(MDBoxLayout):
    tag = StringProperty()
    hint_text = StringProperty()
