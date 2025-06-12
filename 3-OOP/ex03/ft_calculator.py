class calculator:
    def __init__(self, numbers: list[float]):
        self.numbers = numbers

    def __str__(self):
        return str(self.numbers)

    def __add__(self, object) -> None:
        self.numbers = [number + object for number in self.numbers]
        print(self)

    def __mul__(self, object) -> None:
        self.numbers = [number * object for number in self.numbers]
        print(self)

    def __sub__(self, object) -> None:
        self.numbers = [number - object for number in self.numbers]
        print(self)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError("You cannot divide by 0.")
        self.numbers = [number / object for number in self.numbers]
        print(self)