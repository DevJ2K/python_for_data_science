from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """Setter for the variable 'eyes'."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Setter for the variable 'hairs'."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Getter for the variable 'eyes'."""
        return self.eyes

    def get_hairs(self) -> str:
        """Getter for the variable 'hairs'."""
        return self.hairs
