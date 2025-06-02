import sys

def main(args: list[str]) -> None:
    """
    Count the number of characters in a sentence, including upper letters, lower letters, punctuation marks, spaces, and digits."""
    if len(args) == 0 or args[0] == "None":
        words = []
        print("What is the text to count? ", end="")
        while True:
            try:
                value = input()
                words.append("\n" if value == "" else value)
            except EOFError:
                break
        sentence = "".join(words)

    elif len(args) == 1:
        sentence = args[0]
    else:
        raise AssertionError("more than one argument is provided")

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    upper_count = len([char for char in sentence if char.isupper()])
    lower_count = len([char for char in sentence if char.islower()])
    punctuation_count = len([char for char in sentence if char in punctuation])
    space_count = len([char for char in sentence if char.isspace()])
    digit_count = len([char for char in sentence if char.isdigit()])

    print(f"The text contains {upper_count + lower_count + punctuation_count + space_count + digit_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    try:
        main(args=sys.argv[1:])
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected !")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
