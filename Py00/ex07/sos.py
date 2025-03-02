from sys import argv


def convert_to_morse(string: str) -> str:
    """convert_to_morse(string: str) --> str
    :param string: The string to convert to morse
    :return: The string converted into morse
    """
    morse_dict = {" ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ",
                  "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ",
                  "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
                  "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                  "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
                  "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
                  "X": "-..- ", "Y": "-.-- ", "Z": "--.. ", "1": ".----",
                  "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
                  "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
                  "0": "----- "}
    return string.translate(string.maketrans(morse_dict)).removesuffix(" ")


def main():
    try:
        assert len(argv) == 2, "Wrong Number Of Arguments."
        string: str = argv[1]
        for c in string:
            assert c.isalnum() or c == ' ', "Invalid String"
        print(convert_to_morse(string.upper()))
    except AssertionError as err:
        if err.args[0]:
            print("AssertionError:", err)


if __name__ == "__main__":
    main()
