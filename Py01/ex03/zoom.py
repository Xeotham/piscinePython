from PIL import Image, ImageDraw, ImageFont
from load_image import ft_load
from numpy import array, apply_along_axis, uint8


def err_msg(err: int) -> str:
    """Return an error message.

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
    """Translate the coordinate

    Parameters:
        coord (int): Wanted coordinates.
        axis (int): Axis of the coordinate.

    Return:
        int: New coordinate.
    """
    return coord + (axis / 2).__floor__()


def ft_clamp(min_value: int, max_value: int, val: int) -> int:
    """Clamp a value.

    Parameters:
        min_value (int):    Minimum value.
        max_value (int):    Maximum value.
        val (int):          Actual Value.

    Return:
        int: Clamped value.
    """
    return max(min_value, min(val, max_value))


def get_zoom(coord: int, axis: int, zoom: int) -> tuple[int, int]:
    """Get the start position of the zoom.

    Parameters:
        coord (int):    Coordinates.
        axis (int):     Axis.
        zoom (int):     Zoom.

    Return:
        tuple[int, int]: Starting point of the zoom in X and Y axis.
    """
    zoom_ratio: int = (zoom / 2).__floor__()
    coordinate: int = get_coordinates(coord, axis)
    first: int = ft_clamp(0, axis, coordinate - zoom_ratio)
    second: int = ft_clamp(0, axis, coordinate + zoom_ratio)
    if coordinate < zoom_ratio:
        return first, first + zoom
    elif coordinate > axis - zoom_ratio:
        return second - zoom, second
    return first, second


def apply_axes_scaling(img: Image) -> Image:
    """Add scaling on the image.

    Parameters:
        img (Image): Base image.

    Return:
        Image: New image.
    """
    width, height = img.size
    margin = 30
    new_width = width + margin
    new_height = height + margin
    new_image = Image.new("RGB", (new_width, new_height), color="white")
    new_image.paste(img, (margin, 10))
    draw = ImageDraw.Draw(new_image)

    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except OSError or ValueError:
        font = ImageFont.load_default()

        for x in range(0, width, 50):
            draw.line((x + margin, height + 10, x + margin, height + 15),
                      fill="black", width=1)
            draw.text((x + margin, height + 20), str(x), fill="black",
                      font=font)

        for y in range(0, height, 50):
            draw.line((25, y + 10, 30, y + 10), fill="black", width=1)
            draw.text((2, y + 2), str(y), fill="black", font=font)

    return new_image


def main():
    """main()"""
    try:
        arr = ft_load("./animal.jpeg")
        assert arr is not None
        x_pos: int = 100
        y_pos: int = -100
        zoom_size = 400
        x_coords: tuple[int, int] = get_zoom(x_pos, len(arr[0]), zoom_size)
        y_coords: tuple[int, int] = get_zoom(y_pos, len(arr), zoom_size)
        print(arr)
        new_arr: array = array(slice_me([slice_me([
            [x[2]] for x in array(y)], x_coords[0], x_coords[1])
            for y in arr], y_coords[0], y_coords[1])).astype(uint8)
        print("New shape after slicing:", new_arr.shape,
              "or", (len(new_arr), len(new_arr[0])))
        img = apply_axes_scaling(Image.fromarray(new_arr.repeat(3, axis=2)))
        img.show()
        print(new_arr)
    except AssertionError:
        return


if __name__ == "__main__":
    main()
