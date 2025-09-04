from load_csv import load
from pandas import DataFrame
from matplotlib.pyplot import show


def main():
    """Main Program.
    Need to install matplotlib:
    pip install pandas matplotlib
    """
    try:
        loaded_db: DataFrame = load("./population_total.csv")
        assert loaded_db is not None
        countries_info: DataFrame = loaded_db.loc[["France", "Belgium"],
                                                  "1800":"2050"]
        countries_info = countries_info.replace({'[M]': ''},
                                                regex=True).astype(float)
        countries_info = countries_info.T
        countries_info.plot(title="Population Projections",
                            xlabel="Year", ylabel="Population")
        show()

    except AssertionError:
        return 1


if __name__ == "__main__":
    main()
