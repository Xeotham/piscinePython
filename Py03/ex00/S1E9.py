from abc import ABC, abstractmethod


def error_msg(err: int):
    """Function to get all error messages.
    Parameters:
        err (int): index of the error.

    Return:
        str: Error message.
    """
    errors = [
        "Assertion error: first_name isn't a string.",
        "Assertion error: is_alive isn't a boolean."
    ]
    return errors[err]


class Character(ABC):
    """Abstract Class Character."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Character class constructor.
        :param first_name: First name of the character.
        :param is_alive: Boolean to set if the Character is alive.
        """
        assert isinstance(first_name, str), error_msg(0)
        assert isinstance(is_alive, bool), error_msg(1)
        self.first_name: str = first_name
        self.is_alive: bool = is_alive

    def is_alive(self):
        """Method to get if the Character is alive.
        Parameters:
            self: Class instance.
        Return:
            bool: alive attribute of the class.
        """
        return self.is_alive

    def die(self):
        """Method to set the Character alive attribute to False"""
        self.is_alive = False


class Stark(Character):
    """Stark Class inherit from Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor of the Stark Class.
        :param first_name:  First name of the new Stark.
        :param is_alive:    Boolean to set if the new Stark is alive.
        """
        super().__init__(first_name, is_alive)
