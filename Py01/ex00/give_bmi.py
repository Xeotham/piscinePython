def err_msg(err: int) -> str:
    """
    Return an error message.

    Parameters:
        err (int): Index of the error message.

    Return:
        str: Error Message
    """
    errs = ["Both list aren't the same size.",
            "Value aren't of the right type."]
    return errs[err]


def check_values(lst: list[int | float]) -> bool:
    """
    Check if the values of the list is an int or a float.

    Parameters:
        lst (list[int | float]): list of values.

    Return:
        bool: True if all values are in or float, else return False
    """
    try:
        for x in lst:
            assert isinstance(x, int) or isinstance(x, float)
        return True
    except AssertionError:
        return False


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate BMI based on the height and weight.

    Parameters:
        height (list[int | float]): List of height.
        weight (list[int | float]): List of width.

    Return:
        list[int | float]: List of all calculated BMI.
    """
    try:
        assert len(height) == len(weight), err_msg(0)
        assert check_values(height), err_msg(1)
        assert check_values(weight), err_msg(1)
        return [(y / (x ** 2)) for x, y in zip(height, weight)]
    except AssertionError as msg:
        if msg.args[0]:
            print(msg)
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if the BMIs provided is more than the provided limit.

    Parameters:
        bmi (list[int | float]): List of BMI.
        limit (int): Limit of the values.

    Returns:
        list[bool]: List with True if the BMI is more than the limit,
        else False.
    """
    try:
        assert check_values(bmi), err_msg(1)
        assert isinstance(limit, int), err_msg(1)
        return [x > limit for x in bmi]
    except AssertionError as msg:
        if msg.args[0]:
            print(msg)
        return None
