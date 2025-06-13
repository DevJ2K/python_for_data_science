from typing import Any


def callLimit(limit: int):
    """Decorator to limit the number of calls to a function."""
    count = 0

    def callLimiter(function):
        """Inner function that limits the number of calls."""
        def limit_function(*args: Any, **kwds: Any):
            """Function that checks the call limit."""
            nonlocal count
            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
