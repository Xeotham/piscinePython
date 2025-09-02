from PIL import Image
from load_image import zoom_img, apply_axes_scaling, ft_load
from numpy import array, ndarray


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


def rotate_img(img: ndarray) -> ndarray:
    """Rotate the image.

    Parameters:
        img (ndarray): Image to rotate as an array.

    Return:
        ndarray: Array of the rotated image.
    """
    transposed_img = []
    # actual_img = img.tolist()

    for x in range(0, len(img[0]), 1):
        transposed_img.append(array([img[y][x]
                                     for y in range(0, len(img), 1)]))
    return array(transposed_img)


def main():
    """main()"""
    try:
        x_pos: int = 100
        y_pos: int = -100
        zoom_size = 400
        img_arr = ft_load("./animal.jpeg")
        assert img_arr is not None
        img_arr = zoom_img(img_arr, x_pos, y_pos, zoom_size)
        rotated_img = rotate_img(img_arr)
        print("The shape of image is:", img_arr.shape, "or",
              (len(img_arr), len(img_arr[0])))
        print(img_arr)
        print("New shape after Transpose:", (len(rotated_img),
                                             len(rotated_img[0])))
        print(array([array(x).flatten() for x in rotated_img]))
        actual_image = apply_axes_scaling(Image.fromarray(rotated_img
                                                          .repeat(3, axis=2)))
        actual_image.show()
    except AssertionError:
        return


if __name__ == "__main__":
    main()
