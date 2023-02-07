
from View.CollectionScreen.collection_screen import CollectionScreenView


class CollectionScreenController:
    """
    The `CollectionScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.collection_screen.CollectionScreenModel
        self.view = CollectionScreenView(controller=self, model=self.model)

    def get_view(self) -> CollectionScreenView:
        return self.view
