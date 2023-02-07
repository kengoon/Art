if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from typing import Union
from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty, BoundedNumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from Components import path
from kivy.lang import Builder
from textwrap import dedent
from Components.dot import Dot

Builder.load_file(str(path / "spinner" / "spinner.kv"))


class DotSpinner(MDBoxLayout):
    active = BooleanProperty(False)
    dot_num = NumericProperty(5)
    speed = NumericProperty(.5)
    _current_active_dot_index = BoundedNumericProperty(0, min=0, max=dot_num.defaultvalue - 1, errorvalue=0)
    _animating = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clock = None

    def on_kv_post(self, base_widget):
        self.property("_current_active_dot_index").set_max(self, self.dot_num - 1)
        self.add_dots()

    def add_dots(self):
        for i in range(self.dot_num):
            self.add_widget(Dot(current_index=i))

    def get_current_active_dot(self) -> Union[Dot, None]:
        for dot in self.children:
            if dot.active:
                return dot

    def get_dot_index(self, index: int = 0) -> Dot:
        for dot in self.children:
            if dot.current_index == index:
                return dot

    def on_active(self, _, active_value: bool) -> None:
        if active_value:
            self.check_active()
        elif self.clock:
            self.clock.cancel()
            self.deactivate_dots_except()
            self._current_active_dot_index = 0
            self._animating = False

    def check_active(self):
        if self.active and not self._animating:
            self.clock = Clock.schedule_interval(self._animate_spinner, self.speed)
            self._animating = True

    def deactivate_dots_except(self, dot_instance: [Dot, None] = None) -> None:
        for dot in self.children:
            if dot == dot_instance:
                continue
            dot.active = False

    def _animate_spinner(self, _) -> None:
        index_max = self.property("_current_active_dot_index").get_max
        if not self.get_current_active_dot() or (self._current_active_dot_index == index_max):
            dot = self.get_dot_index()
        else:
            self._current_active_dot_index += 1
            dot = self.get_dot_index(self._current_active_dot_index)
        dot.active = True
        self.deactivate_dots_except(dot)


if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivy.lang import Builder


    class Test(MDApp):
        def build(self):
            return Builder.load_string(
                dedent(
                    """
                FloatLayout:
                    DotSpinner
                        active: True
                        dot_num: 5
                        pos_hint:{"center": [.5, .5]}
                        on_touch_down: self.active = False if self.active else True
                """
                )
            )

        # def on_start(self):
        #     self.root.add_widget(DotSpinner(active=True, dot_num=5, pos_hint={"center": [.5, .5]}))


    Test().run()
