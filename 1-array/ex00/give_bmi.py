def input_validator(values: list) -> None:
    """Validate input values for height, weight and bmi.
    Raise AssertionError if invalid."""
    for value in values:
        if not isinstance(value, (int, float)):
            raise AssertionError("All values must be integers or floats.")
        if value <= 0:
            raise AssertionError("All values must be greater than zero.")


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    """Calculate BMI for given height and weight."""

    if len(height) != len(weight):
        raise AssertionError(
            "Height and weight lists must have the same length.")
    input_validator(height)
    input_validator(weight)
    return [x / (y**2) for x, y in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if each BMI value exceeds the given limit."""
    input_validator(bmi)
    if not isinstance(limit, int):
        raise AssertionError("Limit should be an integer.")
    if limit <= 0:
        raise AssertionError("Limit must be greater than zero.")
    return [x > limit for x in bmi]
