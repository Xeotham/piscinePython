from load_csv import load
from pandas import DataFrame
from matplotlib.pyplot import show, scatter, title, xlabel, ylabel


def main():
    """Main Program.
    Need to install matplotlib:
    pip install pandas matplotlib
    """
    try:
        life_expectancy_db: DataFrame = load("./life_expectancy_years.csv")
        income_per_person_db: DataFrame = load(
            "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        assert life_expectancy_db is not None
        assert income_per_person_db is not None

        life_expectancy_db = life_expectancy_db["1900"]
        income_per_person_db = income_per_person_db["1900"]
        print("Life expectancy:", life_expectancy_db)
        print("Income per person:", income_per_person_db)

        scatter(income_per_person_db, life_expectancy_db)
        title("1900")
        xlabel("Gross domestic product")
        ylabel("Life Expectancy")
        show()

    except AssertionError:
        return 1


if __name__ == "__main__":
    main()
