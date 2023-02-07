
from View.PaymentScreen.payment_screen import PaymentScreenView


class PaymentScreenController:
    """
    The `PaymentScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.payment_screen.PaymentScreenModel
        self.view = PaymentScreenView(controller=self, model=self.model)

    def get_view(self) -> PaymentScreenView:
        return self.view
