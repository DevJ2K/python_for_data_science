def square(x: int | float) -> int | float:
    """Calculate the square of x."""
    if not isinstance(x, (int, float)):
        raise ValueError(f"'{x}' should be an integer or a float.")
    return x ** 2


def pow(x: int | float) -> int | float:
    """Calculate the exponent of x by itself."""
    if not isinstance(x, (int, float)):
        raise ValueError(f"'{x}' should be an integer or a float.")
    return x ** x


def outer(x: int | float, function) -> object:
    """outer is use to keep in memory the value of 'count' and \
will returns the inner function that will be call."""
    if not isinstance(x, (int, float)):
        raise ValueError(f"'{x}' should be an integer or a float.")
    count = 0

    def inner() -> float:
        """inner calls function(x) and store value in x. That keep the \
value between calls."""
        nonlocal count, x
        count += 1
        x = function(x)
        return x

    return inner
