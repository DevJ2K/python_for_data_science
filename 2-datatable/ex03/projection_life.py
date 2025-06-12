from load_csv import load
import matplotlib.pyplot as plt
import math


def filter_NaN(df_1: list[float], df_2: list[int]):
    """Remove lines if contains NaN values."""
    new_df_1 = []
    new_df_2 = []

    for v1, v2 in zip(df_1, df_2):
        if not math.isnan(v1) and not math.isnan(v2):
            new_df_1.append(v1)
            new_df_2.append(v2)
    return new_df_1, new_df_2


def main():
    """Load and display ratio life expectancy/income."""
    try:
        df_life_expectancy = load("life_expectancy_years.csv")
        if df_life_expectancy is None:
            return 1

        df_income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if df_income is None:
            return 1

        expectancy_values, income_values = filter_NaN(
            df_life_expectancy["1900"].values,
            df_income["1900"].values)

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        ax.scatter(income_values, expectancy_values)

        fig.canvas.manager.set_window_title("Data visualization")

        ax.set_xlabel("Gross domestic product")
        ax.set_ylabel("Life Expectancy")

        plt.xscale('log')
        ax.set_xticks([300, 1_000, 10_000])
        ax.set_xticklabels(["300", "1k", "10k"])
        ax.set_xlim(300, 10000)
        ax.set_title("1900")

        # ax.plot(x_axis, y_axis)
        plt.show()
        return 0
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    main()
