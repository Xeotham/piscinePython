from PIL import Image, UnidentifiedImageError
from numpy import array, apply_along_axis, uint8, ndarray


def err_msg(err: int) -> str:
    """err_msg(err: int) -> str"""
    errs = ["Lists aren't the same size.",
            "Value aren't of the right type.",
            "File not found.",
            "Image couldn't be opened.",
            "List is None"]
    return errs[err]


def check_size(arr: list) -> bool:
    """check_size(arr: list) -> bool"""
    if isinstance(arr[0], int) or isinstance(arr[0], float):
        return True
    ref_value: int = len(arr[0])
    try:
        for x in arr:
            assert len(x) == ref_value
    except AssertionError:
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me(family: list, start: int, end: int) -> list"""
    try:
        assert isinstance(family, list), err_msg(1)
        assert check_size(family), err_msg(0)
        assert isinstance(start, int), err_msg(1)
        assert isinstance(end, int), err_msg(1)
        arr = apply_along_axis(lambda f_arr: f_arr[slice(start, end)],
                               0, array(family))
        return arr.tolist()
    except AssertionError as msg:
        msg = str(msg)
        if msg:
            print(msg)
        return None


def get_coordinates(coord: int, axis: int) -> int:
    """get_coordinates(coord: int, axis: int) -> int"""
    return coord + (axis / 2).__floor__()


def ft_clamp(min_value: int, max_value: int, val: int) -> int:
    """ft_clamp(min_value: int, max_value: int, val: int) -> int"""
    return max(min_value, min(val, max_value))


def get_zoom(coord: int, axis: int, zoom: int) -> tuple[int, int]:
    """get_zoom(coord: int, axis: int, zoom: int) -> tuple[int, int]"""
    zoom_ratio: int = (zoom / 2).__floor__()
    coordinate: int = get_coordinates(coord, axis)
    first: int = ft_clamp(0, axis, coordinate - zoom_ratio)
    second: int = ft_clamp(0, axis, coordinate + zoom_ratio)
    if coordinate < zoom_ratio:
        return first, first + zoom
    elif coordinate > axis - zoom_ratio:
        return second - zoom, second
    return first, second


def zoom_img(path: str, x_pos: int, y_pos: int, zoom: int):
    img = ft_load(path)
    x_coords: tuple[int, int] = get_zoom(x_pos, len(img[0]), zoom)
    y_coords: tuple[int, int] = get_zoom(y_pos, len(img), zoom)
    new_arr: ndarray = (array(slice_me([slice_me([[x[2]] for x in array(y)],
                                                 x_coords[0], x_coords[1])
                                       for y in img],
                                       y_coords[0], y_coords[1]))
                        .astype(uint8))
    return new_arr


def rotate_img(img: ndarray) -> ndarray:
    return img.transpose((1, 0, 2))


def ft_load(path: str) -> ndarray:
    """ft_load(path: str) -> ndarray"""
    try:
        assert isinstance(path, str), err_msg(1)
        img = Image.open(path)
        assert img != FileNotFoundError, err_msg(2)
        assert img != UnidentifiedImageError, err_msg(3)
        arr = array(img)
        print("The shape of image is:", arr.shape)
        print(arr)
        return arr
    except AssertionError or FileNotFoundError as msg:
        msg = str(msg)
        if msg:
            print(msg)
        return None
