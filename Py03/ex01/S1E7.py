from S1E9 import Character


class Baratheon(Character):
    """Class Baratheon which inherit from the Character class.
    Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon constructor.
        :param first_name: String for the attributes first_name.
        :param is_alive: Boolean for the attributes is_alive.
        """
        super().__init__(first_name, is_alive)

        self.family_name: str = "Baratheon"
        self.eyes: str = "brown"
        self.hairs: str = "dark"

    def __str__(self):
        """Method to create a string.
        :return str: return the stringify class.
        """
        return (f"<bound method Baratheon.__str__ of Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')>")

    def __repr__(self):
        """Method to show arguments.
        :return str: Return values of the class as a string.
        """
        return (f"<bound method Baratheon.__repr__ of Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')>")


class Lannister(Character):
    """Class Lannister which inherit from the Character class,"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Lannister constructor.
        :param first_name: String for the attributes first_name.
        :param is_alive: Boolean for the attributes is_alive.
        """
        super().__init__(first_name, is_alive)

        self.family_name: str = "Lannister"
        self.eyes: str = "blue"
        self.hairs: str = "light"

    def __str__(self):
        """Method to create a string.
        :return str: return the stringify class.
        """
        return (f"<bound method Lannister.__str__ of Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')>")

    def __repr__(self):
        """Method to show arguments.
        :return str: Return values of the class as a string.
        """
        return (f"<bound method Lannister.__repr__ of Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')>")

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool):
        """
        Function to create a new Lannister.
        :param first_name: First name of the new Lannister.
        :param is_alive: Boolean to set if the new Lannister is alive.
        :return: New instance of the Lannister Class.
        """
        return Lannister(first_name, is_alive)
