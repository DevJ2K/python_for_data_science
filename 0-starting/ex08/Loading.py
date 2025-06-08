import os
from typing import Generator

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

        if iteration > 0:
            print(line_clear, end="", flush=True)
        print("\r" + progress_bar, end="", flush=True)

        iteration += 1
        yield i

def ft_tqdm_responsive(lst: range) -> Generator:
    line_clear = '\x1b[2K'
    terminal_size = os.get_terminal_size().columns
    iteration = 1
    for i in lst:
        complete_progress_bar: str = ""
        progression: int = int((iteration / len(lst)) * 100)
        complete_progress_bar += f"{progression}%|".rjust(5)

        after_progress_bar = f"| {iteration}/{len(lst)}"
        after_progress_bar += f"                          "

        animate_progress_bar_size = terminal_size - len(complete_progress_bar) - len(after_progress_bar)

        animate_progress_bar = "█" * int((animate_progress_bar_size * progression) / 100)
        animate_progress_bar += " " * (animate_progress_bar_size - int((animate_progress_bar_size * progression) / 100))

        complete_progress_bar += animate_progress_bar + after_progress_bar
        if iteration > 0:
            print(line_clear, end="", flush=True)
        print("\r" + complete_progress_bar, end="", flush=True)

        iteration += 1
        yield i
