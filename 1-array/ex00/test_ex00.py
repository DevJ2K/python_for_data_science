from give_bmi import give_bmi, apply_limit
import pytest


class TestGiveBmi:
    def test_not_same_args_size(self):
        with pytest.raises(AssertionError):
            give_bmi([3.2, 1.2], [1.2])

    def test_not_a_number(self):
        with pytest.raises(AssertionError):
            give_bmi([3.2, "a"], [1.1, 2])

    def test_contains_0_in_weight(self):
        with pytest.raises(AssertionError):
            give_bmi(height=[3.2, 5.3], weight=[1.1, 0])

    def test_contains_0_in_height(self):
        with pytest.raises(AssertionError):
            give_bmi(height=[3.2, 0], weight=[1.1, 2])

    def test_valid_args(self):
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)

        assert bmi == [22.507863455018317, 29.0359168241966]


class TestApplyLimit:
    def test_bmi_not_a_number(self):
        with pytest.raises(AssertionError):
            apply_limit([3.2, "a"], 30)

    def test_int_not_a_number(self):
        with pytest.raises(AssertionError):
            apply_limit([3.2, "a"], 30.3)
        with pytest.raises(AssertionError):
            apply_limit([3.2, "a"], "a")

    def test_bmi_contains_0(self):
        with pytest.raises(AssertionError):
            apply_limit([0], 30)

    def test_bmi_contains_value_minus_0(self):
        with pytest.raises(AssertionError):
            apply_limit([-1], 30)

    def test_valid_args(self):
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)

        assert apply_limit(bmi, 26) == [False, True]
