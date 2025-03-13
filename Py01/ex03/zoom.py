from PIL import Image
from load_image import ft_load
from numpy import array, apply_along_axis, uint8


def err_msg(err: int) -> str:
    """err_msg(err: int) -> str"""
    errs = ["Lists aren't the same size.",
            "Value aren't of the right type.",
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
        # print("My shape is :", (len(family), len(family[0])))
        arr = apply_along_axis(lambda f_arr: f_arr[slice(start, end)],
                               0, array(family))
        # if arr.any():
        #     print("My new shape is :", (len(arr), len(arr[0])))
        # else:
        #     print("My new shape is : (0, 0)")
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


def main():
    arr = ft_load("./animal.jpeg")
    x_pos: int = -512
    y_pos: int = 384
    zoom_size = 400
    x_coords: tuple[int, int] = get_zoom(x_pos, len(arr[0]), zoom_size)
    y_coords: tuple[int, int] = get_zoom(y_pos, len(arr), zoom_size)
    print(arr)
    new_arr: array = array(slice_me([slice_me([[x[2]] for x in array(y)],
                                    x_coords[0], x_coords[1]) for y in arr],
                                    y_coords[0], y_coords[1])).astype(uint8)
    print("New shape after slicing:", new_arr.shape,
          "or", (len(new_arr), len(new_arr[0])))
    Image.fromarray(new_arr.repeat(3, axis=2)).show()
    print(new_arr)


if __name__ == "__main__":
    main()
