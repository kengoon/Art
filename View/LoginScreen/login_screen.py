from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.LoginScreen.components import (
    LoginMobileScreenView,
    LoginTabletScreenView,
    LoginDesktopScreenView,
)
from View.base_screen import BaseScreenView


class LoginScreenView(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = LoginMobileScreenView
        self.tablet_view = LoginTabletScreenView
        self.desktop_view = LoginDesktopScreenView

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
