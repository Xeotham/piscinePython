from PIL import Image, UnidentifiedImageError
from numpy import array


def err_msg(err: int) -> str:
    """err_msg(err: int) -> str"""
    errs = ["Lists aren't the same size.",
            "Value aren't of the right type.",
            "File not found.",
            "Image couldn't be opened."]
    return errs[err]


def ft_load(path: str) -> array:
    """ft_load(path: str) -> array"""
    try:
        assert isinstance(path, str), err_msg(1)
        img = Image.open(path)
        assert img != FileNotFoundError, err_msg(2)
        assert img != UnidentifiedImageError, err_msg(3)
        arr = array(img)
        print("The shape of image is:", arr.shape)
        return arr
    except AssertionError as msg:
        msg = str(msg)
        if msg:
            print(msg)
        return None
