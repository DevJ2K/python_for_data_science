import sys


def is_integer(value: str):
    """Checks if the given string is a valid integer."""
    if len(value) > 0:
        if value.startswith("-"):
            return len(value) > 1 and value[1:].isdigit()
        return value.isdigit()
    return False


def whatis(n: int):
    """Prints whether the number is even or odd."""
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    pass


def main():
    """Main function to handle command line arguments."""
    try:
        args = sys.argv[1:]
        if len(args) == 0:
            return
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        if not is_integer(args[0]):
            raise AssertionError("argument is not an integer")
        whatis(int(args[0]))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
