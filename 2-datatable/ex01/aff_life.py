from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """Main function to load and print the life expectancy dataset."""
    CITY = "France"
    try:
        df: pd.DataFrame | None = load("life_expectancy_years.csv")
        if df is None:
            return 1

        country_row = df.loc[df["country"] == CITY]
        if country_row.shape[0] == 0:
            print("No line has been found...")
            return 1
        if country_row.shape[1] == 0:
            print("No content to display...")
            return 1

        country_row = country_row.drop(columns=["country"])
        country_row.dropna(axis=1, how="all", inplace=True)

        if country_row.shape[1] == 0:
            print("No content to display...")
            return 1
        elif country_row.shape[1] == 1:
            print("Isn't exist enough datas to display the graph...")
            return 1

        series = country_row.iloc[0]

        x_axis = series.index.astype(int)     # year
        y_axis = series.values.astype(float)  # life expectancy

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        fig.canvas.manager.set_window_title("Data visualization")

        ax.set_xlabel("Year")
        ax.set_ylabel("Life expectancy")

        ax.set_xticks(range(x_axis[0], x_axis[-1], 40))
        ax.set_title(f"{CITY} Life expectancy Projections")

        ax.plot(x_axis, y_axis)
        plt.show()
        return 0
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    main()
