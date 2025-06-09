from array2D import slice_me
import pytest


class TestArray2D:
    """Tests for the slice_me function."""
    def test_one_dimension_array(self):
        with pytest.raises(AssertionError):
            slice_me([1, 2, 3], 0, 2)

    def test_not_a_list(self):
        with pytest.raises(AssertionError):
            slice_me("Salut", 0, 2)

    def test_invalid_index(self):
        with pytest.raises(AssertionError):
            slice_me([[1], [2]], "a", 2)
        with pytest.raises(AssertionError):
            slice_me([[1], [2]], 2, "b")

    def test_invalid_shape(self):
        with pytest.raises(AssertionError):
            slice_me([[1], [1, 2], [3]], 0, 2)

    def test_valid_args(self):
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        assert slice_me(family, 0, 2) == [[1.8, 78.4], [2.15, 102.7]]
        assert slice_me(family, 1, -2) == [[2.15, 102.7]]
