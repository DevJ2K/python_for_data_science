import os
import time

def ft_tqdm(lst: range) -> None:
    line_clear = '\x1b[2K'
    terminal_size = 100
    iteration = 1
    for i in lst:
        progress_bar: str = ""
        progression: int = int((iteration / len(lst)) * 100)
        progress_bar += f"{progression}%|".rjust(5)

        progress_bar += "█" * progression
        progress_bar += " " * (terminal_size - progression)
        progress_bar += f"| {iteration}/{len(lst)}"
        # progress_bar += f" [__:__<__:__, __.__it/s]"

        if iteration > 0:
            print(line_clear, end="", flush=True)
        print("\r" + progress_bar, end="", flush=True)

        iteration += 1
        yield i

# def ft_tqdm_responsive(lst: range) -> None:
#     terminal_size = os.get_terminal_size()
#     for i in lst:
#         print("_", end="", flush=True)
#         yield i

if __name__ == "__main__":
    print(len("[===============================================================>]"))
    print(os.get_terminal_size())
