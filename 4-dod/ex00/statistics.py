from typing import Any

def check_args(*args: Any) -> bool:
    if len(args) == 0:
        return False
    return True

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    OPERATIONS = {
        "mean": lambda x: print(x),
        "median": lambda x: print(x),
        "quartile": lambda x: print(x),
        "std": lambda x: print(x),
        "var": lambda x: print(x)
    }

    if not check_args(*args):
        print("ERROR")
        return

    for key, value in kwargs.items():
        operation = OPERATIONS.get(value)
        if operation is None:
            continue
        operation(value)
        # print(key, value, sep=": ")
