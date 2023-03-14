from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from kivy.properties import OptionProperty, BooleanProperty, ObjectProperty
from kivy.animation import Animation
from Components.effects import LowerScrollEffect, LowerDampedScrollEffect


class RealRecycleView(RecycleView):
    do_swipe = BooleanProperty(False)
    swipe_direction = OptionProperty("horizontal", options=["horizontal", "vertical"], allownone=False)
    effect_cls = ObjectProperty(LowerDampedScrollEffect)

    def __init__(self, **kwargs):
        self.register_event_type('on_real_scroll_stop')  # type: ignore
        self.register_event_type("on_real_scroll_start")
        self.register_event_type("on_swipe_up")
        self.register_event_type("on_swipe_down")
        self.register_event_type("on_swipe_left")
        self.register_event_type("on_swipe_right")
        self.register_event_type("on_overscroll")
        self.register_event_type("on_overscroll_down")
        self.register_event_type("on_overscroll_up")
        super().__init__(**kwargs)
        self.scroll_index = 0
        self._scrolling = False
        self.clock = None
        self._start_touch = None
        self._is_touch_move = False

    def on_scroll_move(self, touch):
        if supra := super().on_scroll_move(touch):
            self._is_touch_move = True
            if self.clock:
                self.clock.cancel()
            self.clock = Clock.schedule_interval(self.check_scrolling, 1)
        return supra

    def on_scroll_start(self, touch, check_children=True):
        if supra := super().on_scroll_start(touch, check_children):
            self.dispatch("on_real_scroll_start")
            self._start_touch = touch.pos
        return supra

    def on_scroll_stop(self, touch, check_children=True):
        if supra := super().on_scroll_stop(touch, check_children):
            self.get_swipe_direction(touch)
        return supra

    def get_swipe_direction(self, touch):
        if not self._start_touch:
            return
        if not self._is_touch_move:
            return
        if self.swipe_direction == "horizontal":
            if self._start_touch[0] < touch.pos[0]:
                self.swipe_right()
                self.dispatch("on_swipe_right")
            else:
                self.swipe_left()
                self.dispatch("on_swipe_left")
        elif self._start_touch[1] < touch.pos[1]:
            self.swipe_up()
            self.dispatch("on_swipe_up")
        else:
            self.swipe_down()
            self.dispatch("on_swipe_down")

        self._start_touch = None
        self._is_touch_move = False

    def on_data(self, *_):
        if self.swipe_direction == "vertical":
            self.scroll_index = len(self.data) - 1

    def swipe_up(self):
        if not self.children:
            return
        if (self.scroll_index > 0 < len(self.data) - 1) and self.do_swipe:
            self.scroll_index -= 1
            child_height = self.children[0].default_height
            scroll = self.convert_distance_to_scroll(0, child_height * self.scroll_index)[1]
            Animation(scroll_y=max(scroll, 0.0), t='out_quad', d=.5).start(self)

    def swipe_down(self):
        if not self.children:
            return
        if (self.scroll_index < len(self.data) - 1) and self.do_swipe:
            self.scroll_index += 1
            child_height = self.children[0].default_height
            scroll = self.convert_distance_to_scroll(0, child_height * self.scroll_index)[1]
            Animation(scroll_y=min(scroll, 1.0), t='out_quad', d=.5).start(self)

    def swipe_left(self):
        if not self.children:
            return
        if (self.scroll_index < len(self.data) - 1) and self.do_swipe:
            self.scroll_index += 1
            child_width = self.children[0].default_width
            scroll = self.convert_distance_to_scroll(child_width * self.scroll_index, 0)[0]
            Animation(scroll_x=min(scroll, 1.0), t='out_quad', d=.5).start(self)

    def swipe_right(self):
        if not self.children:
            return
        if (self.scroll_index > 0 < len(self.data)) and self.do_swipe:
            self.scroll_index -= 1
            child_width = self.children[0].default_width
            scroll = self.convert_distance_to_scroll(child_width * self.scroll_index, 0)[0]
            Animation(scroll_x=max(scroll, 0.0), t='out_quad', d=.5).start(self)

    def on_scroll_y(self, *_):
        self._scrolling = True

    def check_scrolling(self, *_):
        if not self._scrolling:
            self.clock.cancel()
            self.dispatch("on_real_scroll_stop")
        self._scrolling = False

    def on_real_scroll_stop(self):
        pass

    def on_real_scroll_start(self):
        pass

    def on_swipe_up(self):
        pass

    def on_swipe_down(self):
        pass

    def on_swipe_left(self):
        pass

    def on_swipe_right(self):
        pass

    def on_overscroll(self, *args):
        pass

    def on_overscroll_down(self):
        pass

    def on_overscroll_up(self):
        pass
