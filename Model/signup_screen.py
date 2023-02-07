import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class SignupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SignupScreen.signup_screen.SignupScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.SignupScreen.signup_screen.SignupScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("signup screen")

    @multitasking.task
    def check_data(self):
        """Just an example of the method. Use your own code."""

        self.data = ["example item"]
