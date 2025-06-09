import pandas as pd
from pathlib import Path

def load(path: str | Path) -> pd.DataFrame | None:
    """Load a CSV file into a pandas DataFrame."""
    try:
        if isinstance(path, str):
            path: Path = Path(path)
        elif not isinstance(path, Path):
            raise TypeError("The path must be a string or a Path object.")
        if not path.exists():
            raise FileNotFoundError(f"File {path} does not exist.")
        if not path.is_file():
            raise FileNotFoundError(f"Path {path} is not a file.")
        if path.suffix.lower() != '.csv':
            raise ValueError(f"File {path} is not a valid image file.")
        dataframe = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataframe.shape}")
        return dataframe
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
