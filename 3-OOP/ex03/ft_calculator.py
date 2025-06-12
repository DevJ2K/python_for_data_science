class calculator:
    """A calculator to make array operation."""
    def __init__(self, numbers: list[float]):
        """Constructor of the calculator."""
        self.numbers: list[float] = numbers

    def __str__(self):
        """Return the numbers as string."""
        return str(self.numbers)

    def __add__(self, object) -> None:
        """Add 'object' to each numbers."""
        self.numbers = [number + object for number in self.numbers]
        print(self)

    def __mul__(self, object) -> None:
        """Multiply 'object' with each numbers."""
        self.numbers = [number * object for number in self.numbers]
        print(self)

    def __sub__(self, object) -> None:
        """Substract 'object' to each numbers."""
        self.numbers = [number - object for number in self.numbers]
        print(self)

    def __truediv__(self, object) -> None:
        """Divide 'object' to each numbers if 'object' != 0."""
        if object == 0:
            raise ZeroDivisionError("You cannot divide by 0.")
        self.numbers = [number / object for number in self.numbers]
        print(self)
