from sys import argv


def scan_args(string: str):
    """def scan_args(string: str) --> None

scan_args print all the information about the string passed in argument.
ex:
    str = "This is a test"
    print:
        The text contains 14 characters:
        1 upper letters
        10 lower letters
        0 punctuation marks
        3 spaces
        0 digits"""

    print("The text contains", len(string), "characters:")
    print(sum(1 for c in string if c.isupper()), "upper letters")
    print(sum(1 for c in string if c.islower()), "lower letters")
    print(sum(1 for c in string if "\"\'-[]{}()—–…,:;!?.".find(c) != -1),
          "punctuation marks")
    print(sum(1 for c in string if c.isspace()), "spaces")
    print(sum(1 for c in string if c.isdigit()), "digits")


def getInput() -> str:
    """getInput() -> str"""
    try:
        arg: str = input()
        return arg
    except EOFError:
        return getInput()


def main():
    try:
        arg: str = ""
        if (len(argv) <= 1):
            print("What is the text to count?")
            arg = getInput()
        else:
            assert len(argv) == 2, "Invalid number of arguments."
            arg = argv[1]
        scan_args(arg)

    except AssertionError as msg:
        if msg.args[0]:
            print(msg)


if __name__ == "__main__":
    main()
