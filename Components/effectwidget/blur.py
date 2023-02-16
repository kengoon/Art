from kivy.properties import ListProperty
from kivy.uix.effectwidget import EffectWidget, VerticalBlurEffect, HorizontalBlurEffect
from kivymd.uix.behaviors import StencilBehavior


class Blur(EffectWidget, StencilBehavior):
    effects = ListProperty([VerticalBlurEffect(), HorizontalBlurEffect()])
