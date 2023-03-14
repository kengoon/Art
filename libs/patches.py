from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen


def _set_screen(self) -> None:
    """
    Sets the screen according to the type of application screen size:
    mobile/tablet or desktop view.
    """

    if self.real_device_type != self._current_device_type:
        self.clear_widgets()

        if self.mobile_view and self.tablet_view and self.desktop_view:
            if self.real_device_type == "mobile":
                self.add_widget(self.mobile_view.get_instance())
            elif self.real_device_type == "tablet":
                self.add_widget(self.tablet_view.get_instance())
            elif self.real_device_type == "desktop":
                self.add_widget(self.desktop_view.get_instance())

        self.dispatch("on_change_screen_type", self.real_device_type)


MDResponsiveLayout.set_screen = _set_screen


@classmethod
def _get_instance(cls):
    if not cls.__widget:
        cls.__widget = cls()
    return cls.__widget


def _on_enter(self, *args):
    if self.children and isinstance(self.children[0], MDScreen):
        self.children[0].dispatch("on_enter", *args)


MDScreen.__widget = None
MDScreen.get_instance = _get_instance
MDScreen.on_enter = _on_enter
