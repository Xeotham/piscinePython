from pandas.errors import EmptyDataError
from pandas import DataFrame, read_csv


def error_messages(err: int) -> str:
    """Give an error message base of an index
    Parameters:
        err (int): Index of the error message.

    Return:
        str: Error message.
    """

    err_str: list[str] = [
        "Path is None.",
        "File not found:",
        "Permission denied.",
        "The file is empy."
    ]
    return err_str[err]


def load(path: str) -> DataFrame | None:
    """Load a csv file.
    Parameters:
        path (str): Path to the csv file.

    Returns:
        DataFrame: The data frame loaded with the path.
        None: In case of error.
    """

    try:
        assert path, error_messages(0)
        new_csv: DataFrame = read_csv(path, header=0, sep=',',
                                      index_col=0)
        print(f"Loading dataset of dimensions{new_csv.shape}")
        return new_csv
    except AssertionError:
        print(error_messages(0))
        return None
    except FileNotFoundError:
        print(error_messages(1), path, ".")
        return None
    except PermissionError:
        print(error_messages(2))
        return None
    except EmptyDataError:
        print(error_messages(3))
        return None
