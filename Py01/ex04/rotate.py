from PIL import Image
from load_image import zoom_img
from numpy import array, ndarray


def err_msg(err: int) -> str:
    """err_msg(err: int) -> str"""
    errs = ["Lists aren't the same size.",
            "Value aren't of the right type.",
            "List is None"]
    return errs[err]


def rotate_img(img: ndarray) -> ndarray:
    return img.transpose((1, 0, 2))


def main():
    x_pos: int = 0
    y_pos: int = 0
    zoom_size = 400
    img = zoom_img("./animal.jpeg", x_pos, y_pos, zoom_size)
    print("The shape is of image is:", img.shape, "or",
          (len(img), len(img[0])))
    print(img)
    rotated_img: ndarray = rotate_img(img)
    print("New shape after Transpose:", (len(rotated_img),
                                         len(rotated_img[0])))
    print(array([array(x).flatten() for x in rotated_img]))
    Image.fromarray(rotate_img(img).repeat(3, axis=2)).show()


if __name__ == "__main__":
    main()
