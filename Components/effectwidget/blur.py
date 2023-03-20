from kivy.properties import ListProperty, NumericProperty, ReferenceListProperty
from kivy.uix.effectwidget import EffectWidget, VerticalBlurEffect, HorizontalBlurEffect
from kivymd.uix.behaviors import StencilBehavior


class Blur(EffectWidget, StencilBehavior):
    blur_size = ListProperty([0, 0])
    effects = ListProperty([HorizontalBlurEffect(), VerticalBlurEffect()])

    def on_blur_size(self, *args):
        self.effects[0].size, self.effects[1].size = self.blur_size


