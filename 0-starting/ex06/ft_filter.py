from typing import Iterable, Any, Callable


class ft_filter:
    """ft_filter(function or None, iterable) --> ft_filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    def __init__(
            self,
            function: Callable[..., bool],
            iterable: Iterable[Any | None]):
        self.filter = [obj for obj in iterable if function(obj)]

    def __iter__(self):
        return iter(self.filter)
