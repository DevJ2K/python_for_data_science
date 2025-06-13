def square(x: int | float) -> int | float:
    if not isinstance(x, (int, float)):
        raise ValueError(f"'{x}' should be an integer or a float.")
    return x ** 2


def pow(x: int | float) -> int | float:
    if not isinstance(x, (int, float)):
        raise ValueError(f"'{x}' should be an integer or a float.")
    return x ** x


def outer(x: int | float, function) -> object:
    if not isinstance(x, (int, float)):
        raise ValueError(f"'{x}' should be an integer or a float.")
    count = 0

    def inner() -> float:
        nonlocal count, x
        count += 1
        x = function(x)
        return x

    return inner
