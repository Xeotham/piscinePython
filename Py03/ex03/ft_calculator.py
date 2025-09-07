class calculator:
    """Class to make operation of vector with a scalar."""

    def __init__(self, list):
        """
        Calculator Constructor
        :param list: list of object.
        """
        self.list = list

    def __add__(self, object) -> None:
        """
        Overload of the add operator.
        :param object: Object to add to the list.
        """

        self.list = [x + object for x in self.list]
        print(self.list)

    def __mul__(self, object) -> None:
        """
        Overload of the Multiply operator.
        :param object: Object to multiply with.
        """

        self.list = [x * object for x in self.list]
        print(self.list)

    def __sub__(self, object) -> None:
        """
        Overload of the Subtract operator.
        :param object: Object to subtract with.
        """

        self.list = [x - object for x in self.list]
        print(self.list)

    def __truediv__(self, object) -> None:
        """
        Overload of the Divide operator.
        :param object: Object to divide with.
        """

        self.list = [(lambda x: None if object == 0 else x / object)(x)
                     for x in self.list]

        print(self.list)
