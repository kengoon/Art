
from View.ProfileScreen.profile_screen import ProfileScreenView


class ProfileScreenController:
    """
    The `ProfileScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.profile_screen.ProfileScreenModel
        self.view = ProfileScreenView(controller=self, model=self.model)

    def get_view(self) -> ProfileScreenView:
        return self.view
