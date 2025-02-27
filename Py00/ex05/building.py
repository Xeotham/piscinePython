from sys import argv


def main():
    try:
        assert len(argv) == 2, "Invalid number of arguments"
    except AssertionError as msg:
        if (msg.args[0]):
            print(msg)


if __name__ == "__main__":
    main()
