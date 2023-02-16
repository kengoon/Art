from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.lang import Builder
from os.path import join, dirname

Builder.load_file(join(dirname(__file__), "separator.kv"))


class Separator(BoxLayout):
    colors = ListProperty([[0, 0, 0, 0], [0, 0, 0, 1]])
