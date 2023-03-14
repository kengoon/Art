from kivy.clock import Clock
from kivy.metrics import dp

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from kivy.properties import NumericProperty, BoundedNumericProperty, ReferenceListProperty, ObjectProperty, \
    BooleanProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import VariableListProperty
from Components import path
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import StencilBehavior

Builder.load_file(str(path / "card" / "card.kv"))


class StencilCard(MDCard, StencilBehavior):
    pass


class Card(RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    errorhandler = ObjectProperty(lambda x: 1 if x > 1 else 0)
    shadow_r = BoundedNumericProperty(0, min=0.0, max=1.0, errorhandler=errorhandler.defaultvalue)
    shadow_g = BoundedNumericProperty(0, min=0.0, max=1.0, errorhandler=errorhandler.defaultvalue)
    shadow_b = BoundedNumericProperty(0, min=0.0, max=1.0, errorhandler=errorhandler.defaultvalue)
    shadow_color = ReferenceListProperty(shadow_r, shadow_g, shadow_b)
    elevation = NumericProperty(0.005)
    radius = VariableListProperty(dp(10))
    ripple_behavior = BooleanProperty(False)
    md_bg_color = VariableListProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda _: self.on_ripple_behavior(None, self.ripple_behavior))

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def on_ripple_behavior(self, _, value_behavior: bool) -> None:
        self._no_ripple_effect = not value_behavior


if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivy.lang import Builder
    from kivy.animation import Animation
    from random import uniform


    class Test(MDApp):
        def build(self):
            from textwrap import dedent
            return Builder.load_string(
                dedent(
                    """
                # kv_start
                #:import uniform random.uniform
                FloatLayout:
                    Card:
                        size_hint: .5, .5
                        pos_hint: {"center": [.5, .5]}
                        radius: dp(30)
                        shadow_color: 0, 1, 2
                        elevation: 0.01
                        on_release: self.shadow_color=[uniform(0, 1), uniform(0, 1), uniform(0, 1)]
                # kv_end
                """
                )
            )

    Test().run()
