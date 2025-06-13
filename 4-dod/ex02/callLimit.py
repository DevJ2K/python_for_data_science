from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
