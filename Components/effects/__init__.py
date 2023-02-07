from kivy.effects.scroll import ScrollEffect
from kivy.properties import NumericProperty


class LowerScrollEffect(ScrollEffect):
    friction = NumericProperty(0.02)


class HardStopScrollEffect(LowerScrollEffect):
    def stop(self, val, t=None):
        return super().stop(val, t=0.01)
