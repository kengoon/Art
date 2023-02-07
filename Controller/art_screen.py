
from View.ArtScreen.art_screen import ArtScreenView


class ArtScreenController:
    """
    The `ArtScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.art_screen.ArtScreenModel
        self.view = ArtScreenView(controller=self, model=self.model)

    def get_view(self) -> ArtScreenView:
        return self.view
