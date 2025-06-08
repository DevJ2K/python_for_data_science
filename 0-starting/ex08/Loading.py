import os
from typing import Generator


def ft_tqdm(lst: range) -> None:
    """
    A simple progress bar that displays the percentage of completion
    and the current iteration out of the total number of iterations.
    """

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
    """
    A simple progress bar that displays the percentage of completion
    and the current iteration out of the total number of iterations.
    """

    line_clear = '\x1b[2K'
    terminal_size = os.get_terminal_size().columns
    iteration = 1
    for i in lst:
        complete_progress_bar: str = ""
        progression: int = int((iteration / len(lst)) * 100)
        complete_progress_bar += f"{progression}%|".rjust(5)

        after_progress_bar = f"| {iteration}/{len(lst)}"
        after_progress_bar += "                          "

        animate_progress_bar_size = terminal_size
        animate_progress_bar_size -= len(complete_progress_bar)
        animate_progress_bar_size -= len(after_progress_bar)

        nb_bloc = int((animate_progress_bar_size * progression) / 100)
        animate_progress_bar = "█" * nb_bloc
        animate_progress_bar += " " * (animate_progress_bar_size - nb_bloc)

        complete_progress_bar += animate_progress_bar + after_progress_bar
        if iteration > 0:
            print(line_clear, end="", flush=True)
        print("\r" + complete_progress_bar, end="", flush=True)

        iteration += 1
        yield i
