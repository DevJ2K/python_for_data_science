from typing import Any


def check_args(args: tuple[float]) -> bool:
    if len(args) == 0:
        return False
    if any([not isinstance(x, (int, float)) for x in args]):
        return False
    return True


def floor(nb: float) -> int:
    return int(nb // 1)


def percentile(args: tuple[float], percentage: int) -> float:
    args = list(args)
    args.sort()

    percentage /= 100
    pos = percentage * (len(args) - 1)

    rest_pos = pos - floor(pos)
    int_pos = floor(pos)

    if int_pos == len(args):
        next_pos = int_pos
    else:
        next_pos = int_pos + 1

    nb = args[next_pos] - args[int_pos]
    nb_to_add = nb * rest_pos
    return args[int_pos] + nb_to_add


def mean(args: tuple[float]) -> float:
    return sum(args) / len(args)


def variance(args: tuple[float]) -> float:
    mean_args = mean(args)
    return sum([(x - mean_args) ** 2 for x in args]) / (len(args))


def standard_deviation(args: tuple[float]) -> float:
    return variance(args) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    OPERATIONS = {
        "mean": lambda x: f"mean : {mean(x)}",
        "median": lambda x: f"median : {percentile(x, 50)}",
        "quartile": lambda x: f"quartile : \
{[percentile(x, 25), percentile(x, 75)]}",
        "std": lambda x: f"std : {standard_deviation(x)}",
        "var": lambda x: f"var : {variance(x)}"
    }

    for _, value in kwargs.items():
        if not check_args(args):
            print("ERROR")
            continue
        operation = OPERATIONS.get(value)
        if operation is None:
            continue
        print(operation(args))
