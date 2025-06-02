import sys


NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def is_valid_string(string: str):
    """
    Check if the string contains only alphanumeric or space."""
    return all([c.upper() in NESTED_MORSE.keys() for c in string])


def main(args: list[str]) -> None:
    if len(args) != 1 or not is_valid_string(args[0]):
        raise AssertionError("the arguments are bad")
    converted_values = [NESTED_MORSE[c.upper()] for c in args[0]]
    print(" ".join(converted_values))


if __name__ == "__main__":
    try:
        main(args=sys.argv[1:])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
