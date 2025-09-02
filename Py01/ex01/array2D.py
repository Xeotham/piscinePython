from numpy import array, apply_along_axis


def err_msg(err: int) -> str:
    """
    Return an error message.

    Parameters:
        err (int): Index of the error message.

    Return:
        str: Error Message
    """
    errs = ["Lists aren't the same size.",
            "Value aren't of the right type.",
            "List is None"]
    return errs[err]


def check_size(arr: list) -> bool:
    """
    Check if the lists are all the same size.

    Parameters:
        arr (list): list of list.

    Return:
        bool: True if all lists are the same size, else return False
    """
    ref_value: int = len(arr[0])
    try:
        for x in arr:
            assert len(x) == ref_value
    except AssertionError:
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """Slice the given list

    Parameters:
        family (list):  List of list to slice.
        start (int):    Start of the slice.
        end (int):      End of the slice.

    Return:
        list: The sliced list.
    """
    try:
        assert isinstance(family, list), err_msg(1)
        assert check_size(family), err_msg(0)
        assert isinstance(start, int), err_msg(1)
        assert isinstance(end, int), err_msg(1)
        print("My shape is :", (len(family), len(family[0])))
        arr = apply_along_axis(lambda f_arr: f_arr[slice(start, end)],
                               0, array(family))
        if arr.any():
            print("My new shape is :", (len(arr), len(arr[0])))
        else:
            print("My new shape is : (0, 0)")
        return arr.tolist()
    except AssertionError as msg:
        msg = str(msg)
        if msg:
            print(msg)
        return None
