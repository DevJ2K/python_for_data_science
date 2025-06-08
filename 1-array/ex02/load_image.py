import numpy as np
from pathlib import Path
from PIL import Image

def ft_load(path: str | Path) -> np.ndarray:
    #your code here

    if isinstance(path, str):
        path: Path = Path(path)
    elif not isinstance(path, Path):
        raise TypeError("The path must be a string or a Path object.")
    if not path.exists():
        raise FileNotFoundError(f"File {path} does not exist.")
    if not path.is_file():
        raise FileNotFoundError(f"Path {path} is not a file.")
    if not path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
        raise ValueError(f"File {path} is not a valid image file.")
    try:
        image = Image.open(path)
        image = image.convert("RGB")
        image_array: np.ndarray = np.array(image)
        print(f"The shape of image is: {image_array.shape}")
        return image_array
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the image: {e}")
