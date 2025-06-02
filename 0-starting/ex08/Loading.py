def ft_tqdm(lst: range) -> None:
    for i in lst:
        print("_", end="", flush=True)
        yield i