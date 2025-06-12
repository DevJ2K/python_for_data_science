from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        if not isinstance(first_name, str):
            raise ValueError("'first_name' should be a string.")
        if not isinstance(is_alive, bool):
            raise ValueError("'is_alive' should be a boolean.")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None: ...


class Stark(Character):
    """Your docstring for Class"""
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
        return
