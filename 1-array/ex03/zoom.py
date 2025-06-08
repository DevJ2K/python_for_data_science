from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def zoom(
        array: np.ndarray,
        left: int,
        top: int,
        right: int,
        bottom: int) -> np.ndarray:
    """
    Zoom into a specific area of the image defined by the coordinates.
    """
    return array[top:bottom, left:right, :]


def hex_to_grayscale(x: np.ndarray):
    """
    Convert a hex RGB value to grayscale."""
    return int(np.sum(x) / 3)


def to_grayscale(array: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image array to a grayscale image array.
    """
    return np.expand_dims(
        np.apply_along_axis(hex_to_grayscale, axis=2, arr=array),
        axis=2)


def main():
    """
    Main function to execute the zoom functionality.
    """
    try:
        array_image = ft_load("animal.jpeg")
        print(array_image)

        zoomed_image: np.ndarray = zoom(
            array_image, left=450, top=100, right=850, bottom=500)

        gray_image = to_grayscale(zoomed_image)
        print(f"New shape after slicing: {gray_image.shape}")
        print(gray_image)

        plt.imshow(
            to_grayscale(gray_image),
            cmap='gray',
            interpolation='nearest')
        plt.show()
    except Exception as e:
        print(f"Error loading image: {e}")
        return


if __name__ == "__main__":
    main()
