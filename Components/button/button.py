from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, OptionProperty, ColorProperty, VariableListProperty
from kivy.lang import Builder
import kivymd.uix.button.button
from kivy.resources import resource_find
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from Components import path
from Components.card import Card
from kivymd.uix.card import MDCard
Builder.load_file(str(path / "button" / "button.kv"))


class RoundImageButton(ButtonBehavior, Widget):
    source = StringProperty()


class OutlineIconButton(MDCard):
    md_font = StringProperty(resource_find("materialdesignicons-webfont.ttf"))
    font_name = StringProperty()
    theme_icon_color = OptionProperty("Primary", options=kivymd.uix.button.button.theme_text_color_options)
    icon_color = ColorProperty()
    icon = StringProperty()
    font_style = StringProperty("Icons")


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

