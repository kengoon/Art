from kivy.effects.scroll import ScrollEffect
from kivy.properties import NumericProperty
from kivy.effects.dampedscroll import DampedScrollEffect


class LowerScrollEffect(ScrollEffect):
    friction = NumericProperty(0.03)

    def on_overscroll(self, *args):
        sv = self.target_widget.parent
        if hasattr(sv, "on_overscroll"):
            sv.dispatch("on_overscroll", *args)
            if args[1] < 0:
                sv.dispatch("on_overscroll_down")
            else:
                sv.dispatch("on_overscroll_up")


class HardStopScrollEffect(LowerScrollEffect):
    def stop(self, val, t=None):
        return super().stop(val, t=0.01)


class LowerDampedScrollEffect(DampedScrollEffect):
    friction = NumericProperty(.03)

    def on_overscroll(self, *args):
        super().on_overscroll(*args)
        sv = self.target_widget.parent
        if hasattr(sv, "on_overscroll"):
            sv.dispatch("on_overscroll", *args)
            if args[1] < 0:
                sv.dispatch("on_overscroll_down")
            else:
                sv.dispatch("on_overscroll_up")


class HardStopDampedScrollEffect(LowerDampedScrollEffect):
    def stop(self, val, t=None):
        return super().stop(val, t=0.01)
