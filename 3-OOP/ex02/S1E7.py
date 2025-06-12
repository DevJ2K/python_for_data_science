from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor will init Baratheon by calling Character constructor.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """Return the class as string."""
        return str(f"Vector: {(self.family_name, self.eyes, self.hairs)}")

    def __repr__(self) -> str:
        """Return the class representation."""
        return str(f"Vector: {(self.family_name, self.eyes, self.hairs)}")

    def die(self):
        """Pass the is_alive variable of Character to False."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor will init Lannister by calling Character constructor.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        """Return the class as string."""
        return str(f"Vector: {(self.family_name, self.eyes, self.hairs)}")

    def __repr__(self) -> str:
        """Return the class representation."""
        return str(f"Vector: {(self.family_name, self.eyes, self.hairs)}")

    def die(self):
        """Pass the is_alive variable of Character to False."""
        self.is_alive = False

    @staticmethod
    def create_lannister(name: str, is_alive: bool) -> "Lannister":
        """A static method to create a Lannister."""
        return Lannister(name, is_alive)
