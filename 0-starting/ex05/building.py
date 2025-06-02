import sys


def main(args: list[str]) -> None:
    """
    Count the number of characters in a sentence, including upper letters,
    lower letters, punctuation marks, spaces, and digits."""
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

    nb_upper = len([char for char in sentence if char.isupper()])
    nb_lower = len([char for char in sentence if char.islower()])
    nb_punctuation = len([char for char in sentence if char in punctuation])
    nb_space = len([char for char in sentence if char.isspace()])
    nb_digit = len([char for char in sentence if char.isdigit()])

    sum_count = nb_upper + nb_lower + nb_punctuation + nb_space + nb_digit

    print(f"The text contains {sum_count} characters:")
    print(f"{nb_upper} upper letters")
    print(f"{nb_lower} lower letters")
    print(f"{nb_punctuation} punctuation marks")
    print(f"{nb_space} spaces")
    print(f"{nb_digit} digits")


if __name__ == "__main__":
    try:
        main(args=sys.argv[1:])
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected !")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
