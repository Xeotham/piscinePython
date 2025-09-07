from S1E7 import Baratheon, Lannister


def error_msg(err: int):
    """Function that return an error message.
    Parameters:
        err (int): Index of the error.

    Return:
        str: Error message.
    """

    error = [
        "AssertionError: Value provided to set_eyes isn't a string.",
        "AssertionError: Value provided to set_hairs isn't a string."
    ]
    return error[err]


class King(Baratheon, Lannister):
    """King Class which inherit from Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """King Class constructor.
        :param first_name: String for the attributes first_name.
        :param is_alive: Boolean for the attributes is_alive.
        """

        super().__init__(first_name, is_alive)

    def set_eyes(self, new_value: str):
        """Setter for the eyes attributes.
        :param new_value: New value for the attributes eyes."""

        assert isinstance(new_value, str), error_msg(0)
        self.eyes = new_value

    def set_hairs(self, new_value: str):
        """Setter for the hairs attributes.
        :params new_value: New value for the attributes hairs.
        """

        assert isinstance(new_value, str), error_msg(1)
        self.hairs = new_value

    def get_eyes(self):
        """Getter for the eyes attributes.
        :return eyes: Value of the attributes eyes.
        """

        return self.eyes

    def get_hairs(self):
        """Getter for the heirs attributes.
        :return hairs: Value of the attributes hairs.
        """

        return self.hairs
