def get_shape(lst: list[list]) -> str:
    y_shape = len(lst)
    if y_shape == 0:
        return "(0, 0)"
    return f"({y_shape}, {len(lst[0])})"


def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of the family list from start to end."""

    if not isinstance(family, list):
        raise AssertionError("Family must be a list.")
    if not all(isinstance(member, list) for member in family):
        raise AssertionError("Each family member must be a list.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("Start and end indices must be integers.")
    if not all([len(member) == len(family[0]) for member in family]):
        raise AssertionError(
            "All family members must have the same number of attributes.")
    print(f"My shape is : {get_shape(family)}")
    new_family = family[start:end]
    print(f"My new shape is : {get_shape(new_family)}")
    return new_family
