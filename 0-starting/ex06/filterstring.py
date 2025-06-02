import sys
from ft_filter import ft_filter


def main(args: list[str]) -> None:
    """
    Main function to filter words based on their length from the input string.
    The first argument is the string to filter, and the second argument is the
    minimum length a word must have to be included in the output.
    If the arguments are not valid, an AssertionError is raised."""
    if len(args) != 2 or not args[1].isdigit():
        raise AssertionError("the arguments are bad")

    output = ft_filter(lambda x: len(x) > int(args[1]), args[0].split())

    print(list(output))


def test(args: list[str]) -> None:
    """Test the ft_filter function with the provided arguments."""
    expected = filter(lambda x: len(x) > int(args[1]), args[0].split())
    mine = ft_filter(lambda x: len(x) > int(args[1]), args[0].split())

    list_expected = list(expected)
    list_mine = list(mine)

    assert list_expected == list_mine


if __name__ == "__main__":
    try:
        main(args=sys.argv[1:])
        test(args=sys.argv[1:])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
