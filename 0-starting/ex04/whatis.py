import sys

def is_integer(value: str):
    if len(value) > 0:
        if value.startswith("-"):
            return len(value) > 1 and value[1:].isdigit()
        return value.isdigit()
    return False

def whatis(n: int):
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    pass

def main(args: list[str]):
    if len(args) == 0:
        return
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    if not is_integer(args[0]):
        raise AssertionError("argument is not an integer")
    whatis(int(args[0]))

if __name__ == "__main__":
    try:
        main(args=sys.argv[1:])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
