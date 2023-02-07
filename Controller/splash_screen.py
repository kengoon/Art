
from View.SplashScreen.splash_screen import SplashScreenView


class SplashScreenController:
    """
    The `SplashScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.splash_screen.SplashScreenModel
        self.view = SplashScreenView(controller=self, model=self.model)

    def get_view(self) -> SplashScreenView:
        return self.view
