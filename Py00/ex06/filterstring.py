from sys import argv
from ft_filter import ft_filter


def err_msg():
    """
    err_msg() --> string
    :return: Return the error message "AssertionError: the arguments are bad"
    """
    return "AssertionError: the arguments are bad"


def test_input(s: str, n: int):
    """test_input(s: str, n: int): --> None
:param s: The string to test
:param n: The number of character each word should have to be printed"""
    # Test to compare filter with ft_filter
    # r_filter_result = filter(lambda str: len(str) >= n, s.split(' '))
    # ft_filter_result = ft_filter(lambda str: len(str) >= n, s.split(' '))
    # print("Real filter doc:", filter.__doc__, end="\n\n")
    # print("ft_filter doc:", ft_filter.__doc__)
    # print("Real filter result:", r_filter_result, end="\n")
    # print("ft_filter result:", ft_filter_result, end="\n\n")
    # print("Real filter result list:", tuple(r_filter_result), end="\n")
    # print("ft_filter result list:", tuple(ft_filter_result))
    #
    # Real Test
    print(list(ft_filter(lambda str: len(str) >= n, s.split(' '))))


def main():
    try:
        assert len(argv) == 3, err_msg()
        assert argv[2].isdigit() is True, err_msg()
        # print(ft_filter.__doc__) # Test for ft_filter.__doc__
        test_input(argv[1], int(argv[2]))
    except AssertionError as msg:
        if msg.args[0]:
            print(msg)


if __name__ == "__main__":
    main()
