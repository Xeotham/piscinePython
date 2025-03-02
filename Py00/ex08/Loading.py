# import os
# import fcntl
# import termios
# import struct


def get_terminal_size() -> int:
    """get_terminal_size() -> int"""
    # # Get the file descriptor for stdout
    # fd = os.open(os.ctermid(), os.O_RDONLY)
    # try:
    #     # Get the terminal size using an ioctl call
    #     size = fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234')
    #     size = struct.unpack('hh', size)
    #     size = size[1]
    # except Exception:
    #     size = 80 # Default size if unable to get actual size
    # finally:
    #     os.close(fd)
    size = 80
    return size


def get_color(percent: int) -> str:
    """get_color(percent: int) -> str"""
    start_color = [255, 0, 0]
    end_color = [0, 255, 0]
    ratio = (percent % 50) / 50

    if percent < 50:
        r = start_color[0]
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
    else:
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = end_color[1]
    b = 0
    return f"\x1b[38;2;{r};{g};{b}m"


def create_bar(advancement: int, base: int) -> str:
    """create_bar(advancement: int, base: int) --> str"""
    loading: str = "▏▎▍▌▋▊▉█"
    i: int = 0
    percent: int = ((100 * advancement) / base).__floor__()
    bar: str = ""
    for loop in range(len(str(percent)), 3):
        bar += ' '
    bar += str(percent) + "%["
    bar_len: int = (get_terminal_size() - len(bar)
                    - 1 - len(f"\x1b[0m]{advancement}/{base}"))
    if percent < 100:
        bar += get_color(percent)
    else:
        bar += "\x1b[38;2;0;255;0m"
    for loop in range(0, ((bar_len * advancement) / base).__floor__()):
        bar += "█"
        i += 1
    bar += loading[((advancement * (bar_len * 8)) / base % 8).__floor__()]
    for loop in range(i, bar_len):
        bar += " "
    bar += f"\x1b[0m\b]{advancement}/{base}"
    return bar


def ft_tqdm(lst: range) -> None:
    """ft_tqdm(lst: range) --> None"""
    for i, elem in enumerate(lst):

        bar: str = create_bar(i + 1, len(lst))
        i += 1
        print(bar, end='\r')
        yield elem
    print()
