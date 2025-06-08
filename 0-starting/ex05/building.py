import sys


def main():
    """
    Count the number of characters in a sentence, including upper letters,
    lower letters, punctuation marks, spaces, and digits."""
    try:
        args = sys.argv[1:]
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

        nb_upper = len([c for c in sentence if c.isupper()])
        nb_lower = len([c for c in sentence if c.islower()])
        nb_punctuation = len([c for c in sentence if c in punctuation])
        nb_space = len([c for c in sentence if c.isspace()])
        nb_digit = len([c for c in sentence if c.isdigit()])

        sum_count = nb_upper + nb_lower + nb_punctuation + nb_space + nb_digit

        print(f"The text contains {sum_count} characters:")
        print(f"{nb_upper} upper letters")
        print(f"{nb_lower} lower letters")
        print(f"{nb_punctuation} punctuation marks")
        print(f"{nb_space} spaces")
        print(f"{nb_digit} digits")
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected !")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
