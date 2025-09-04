from load_csv import load
from pandas import DataFrame
from matplotlib.pyplot import show


def main():
    """Main Program.
    Need to install matplotlib:
    pip install pandas matplotlib
    """
    try:
        loaded_db: DataFrame = load("./life_expectancy_years.csv")
        assert loaded_db is not None
        france_info: DataFrame = loaded_db.loc["France"]
        france_info.plot(title="France Life expectancy Projections",
                         xlabel="Year", ylabel="Life expectancy")
        show()

    except AssertionError:
        return 1


if __name__ == "__main__":
    main()
