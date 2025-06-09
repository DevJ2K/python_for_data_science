import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert the colors of the image represented by the array.
    """
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel from the image represented by the array.
    """
    new_array = array.copy()
    new_array[:, :, 1:] = 0
    return new_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel from the image represented by the array.
    """
    new_array = array.copy()
    new_array[:, :, ::2] = 0
    return new_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel from the image represented by the array.
    """
    new_array = array.copy()
    new_array[:, :, :2] = 0
    return new_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert the image represented by the NumPy array \
to grayscale using the average of the RGB channels.
    """
    return np.mean(array, axis=2)
