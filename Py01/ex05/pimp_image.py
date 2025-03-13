from numpy import apply_along_axis, uint8, ndarray


def ft_invert(img: ndarray) -> ndarray:
    """Inverts the color of the image received."""
    return (apply_along_axis(lambda colors: [255 - colors[0], 255 - colors[1],
                                             255 - colors[2]], 2, img)
            .astype(uint8))


def ft_red(img: ndarray) -> ndarray:
    """Apply a red filter to the image received."""
    return (apply_along_axis(lambda colors: [colors[0], 0, 0], 2, img)
            .astype(uint8))


def ft_green(img: ndarray) -> ndarray:
    """Apply a green filter to the image received."""
    return (apply_along_axis(lambda colors: [0, colors[1], 0], 2, img)
            .astype(uint8))


def ft_blue(img: ndarray) -> ndarray:
    """Apply a blue filter to the image received."""
    return (apply_along_axis(lambda colors: [0, 0, colors[2]], 2, img)
            .astype(uint8))


def ft_grey(img: ndarray) -> ndarray:
    """Apply a grey filter to the image received."""
    return (apply_along_axis(lambda colors: [colors[0], colors[0], colors[0]],
                             2, img)
            .astype(uint8))
