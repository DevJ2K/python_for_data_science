class calculator:
    """A calculator to make operation between two vectors."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Make the dot product between two vectors."""
        value = sum([x1 * x2 for x1, x2 in zip(V1, V2)])
        print(f"Dot product is: {value}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Make the sum between two vectors."""
        value = [float(x1 + x2) for x1, x2 in zip(V1, V2)]
        print(f"Add Vector is: {value}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Make the substraction between two vectors."""
        value = [float(x1 - x2) for x1, x2 in zip(V1, V2)]
        print(f"Sous Vector is: {value}")
