from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import numpy as np
from PIL import Image


def show_image(array: np.ndarray, mode: str = 'RGB') -> None:
    """Display an image represented by a NumPy array.
    """
    if mode == 'L':
        img = Image.fromarray(np.uint8(array), mode)
    elif mode == 'RGB':
        img = Image.fromarray(array, mode)
    else:
        raise ValueError(f"'{mode}' is not a valid mode.")
    img.show()


def main():
    """Main function to demonstrate the image processing functions.
    """
    array = ft_load("landscape.jpg")
    print(f"The shape of image is: {array.shape}")
    print(array)

    invert_array = ft_invert(array)
    red_array = ft_red(array)
    green_array = ft_green(array)
    blue_array = ft_blue(array)
    grey_array = ft_grey(array)
    print(" ==== DOCUMENTATION ==== ")
    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    print(ft_green.__doc__)
    print(ft_blue.__doc__)
    print(ft_grey.__doc__)

    input("Press Enter to show original image...")
    show_image(array)

    input("Press Enter to show inverted image...")
    show_image(invert_array)

    input("Press Enter to show red filtered image...")
    show_image(red_array)

    input("Press Enter to show green filtered image...")
    show_image(green_array)

    input("Press Enter to show blue filtered image...")
    show_image(blue_array)

    input("Press Enter to show grey image...")
    show_image(grey_array, mode='L')


if __name__ == "__main__":
    main()
