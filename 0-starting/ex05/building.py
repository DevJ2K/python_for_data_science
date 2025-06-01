import sys

def main(args):
    pass


if __name__ == "__main__":
    try:
        main(args=sys.argv[1:])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
