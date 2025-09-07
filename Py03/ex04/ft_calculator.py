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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Function to make the dot product of two vectors.
        :param V1: First Vector
        :param V2: Second Vector
        """

        vect_add = [x * y for x, y in zip(V1, V2)]
        result = 0
        for nb in vect_add:
            result += nb
        print("Dot Product is: ", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Function to make the sum of two vectors.
        :param V1: First Vector.
        :param V2: Second Vector.
        :return:
        """

        result = [x + y for x, y in zip(V1, V2)]
        print("Add vector is : ", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Function to make the subtraction of two vectors.
        :param V1: First Vector.
        :param V2: Second Vector.
        :return:
        """

        result = [x - y for x, y in zip(V1, V2)]
        print("Add vector is : ", result)
