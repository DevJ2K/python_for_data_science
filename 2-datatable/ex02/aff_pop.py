from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def convert_string_to_number(number_str: str) -> float:
    """Convert the number in string format to float."""
    try:
        unit = number_str[-1]
        try:
            index = ['', 'K', 'M', 'G', 'T', 'P'].index(unit.upper())
        except ValueError:
            index = 0
        if index == 0:
            return float(number_str)
        number = float(number_str[:-1])
        for _ in range(index):
            number *= 1000
        return number

    except Exception:
        raise ValueError("Please provide a number in a valid format.")


def convert_number_to_string(num: float):
    """Convert the number to string format."""
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.0f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


def get_ticks(axis_1: list, axis_2: list, step: int = 20_000_000):
    """Get the ticks for the axis based on the two axes provided."""
    max_value = max(max(axis_1), max(axis_2))
    min_value = min(min(axis_1), min(axis_2))
    values = []
    while min_value < max_value:
        values.append(min_value)
        min_value += step
    return values


def get_axis(df: pd.DataFrame, city: str) -> tuple | None:
    """Get the x and y axis data for a given city from the DataFrame."""
    country_row = df.loc[df["country"] == city]
    if country_row.shape[0] == 0:
        print("No line has been found...")
        return None

    country_row = country_row.drop(columns=["country"])
    country_row.dropna(axis=1, how="all", inplace=True)

    years = [col for col in country_row.columns
             if col.isdigit() and 1800 <= int(col) <= 2050]
    country_row = country_row[years]

    if country_row.shape[1] == 0:
        print("No content to display...")
        return None
    elif country_row.shape[1] == 1:
        print("Isn't exist enough datas to display the graph...")
        return None

    series = country_row.iloc[0]
    series = series.apply(convert_string_to_number)

    x_axis = series.index.astype(int)
    y_axis = series.values

    return (x_axis, y_axis)


def main():
    """Main function to load and print the life expectancy dataset."""
    CITY_1 = "France"
    CITY_2 = "Belgium"
    try:
        df: pd.DataFrame | None = load("population_total.csv")
        if df is None:
            return 1

        fig, ax = plt.subplots(1, 1)

        fig.canvas.manager.set_window_title("Data visualization")

        axis_city_1 = get_axis(df, CITY_1)
        if axis_city_1 is None:
            return
        axis_city_2 = get_axis(df, CITY_2)
        if axis_city_2 is None:
            return

        ax.plot(*axis_city_1, c="g")
        ax.plot(*axis_city_2, c="b")

        ax.set_xlabel("Year")
        ax.set_ylabel("Population")

        ax.set_xticks(range(1800, 2050, 40))

        # y_ticks = get_ticks(axis_city_1[1], axis_city_2[1])
        y_ticks = [20_000_000, 40_000_000, 60_000_000]

        ax.set_yticks(y_ticks)
        ax.set_yticklabels([convert_number_to_string(tick)
                            for tick in y_ticks])

        ax.legend([CITY_1, CITY_2], loc='lower right')

        ax.set_title("Population Projections")

        plt.show()
        return 0
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    main()
