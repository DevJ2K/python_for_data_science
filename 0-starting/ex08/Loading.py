import os


def ft_tqdm(lst: range) -> None:
    terminal_size = os.get_terminal_size()
    for i in lst:
        print("_", end="", flush=True)
        yield i

if __name__ == "__main__":
    print(os.get_terminal_size())
