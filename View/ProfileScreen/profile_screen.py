from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.ProfileScreen.components import (
    MobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView


class ProfileScreenView(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileScreenView()
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
