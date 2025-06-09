from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """Main function to load and print the life expectancy dataset."""
    try:
        df: pd.DataFrame | None = load("life_expectancy_years.csv")
        if df is None:
            return 1
        # print(df)
        france_row = df.loc[df["country"] == "France"]
        if france_row.shape[0] == 0:
            print("No line has been found...")
            return 1
        print(france_row)
        france_row = france_row.drop(columns=["country"])
        print(france_row)

        france_row.cumsum()
        france_row.plot()
        # print(france_row[1:])
        return 0
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    main()
