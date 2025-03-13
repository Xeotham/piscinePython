def err_msg(err: int) -> str:
    """err_msg(err: int) -> str"""
    errs = ["Both list aren't the same size.",
            "Value aren't of the right type."]
    return errs[err]


def check_values(lst: list[int | float]) -> bool:
    """check_values(lst: list[int | float]) -> bool"""
    try:
        for x in lst:
            assert isinstance(x, int) or isinstance(x, float)
        return True
    except AssertionError:
        return False


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """give_bmi(height: list[int | float], weight: list[int | float])
-> list[int | float]"""
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
    """apply_limit(bmi: list[int | float], limit: int) -> list[bool]"""
    try:
        assert check_values(bmi), err_msg(1)
        assert isinstance(limit, int), err_msg(1)
        return [x > limit for x in bmi]
    except AssertionError as msg:
        if msg.args[0]:
            print(msg)
        return None
