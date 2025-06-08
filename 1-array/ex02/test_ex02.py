from load_image import ft_load
from pathlib import Path
import pytest


class TestFtLoad:
    def test_valid_file(self):
        result = ft_load("landscape.jpg")
        assert result.shape == (257, 450, 3)

    def test_file_not_exist(self):
        with pytest.raises(FileNotFoundError):
            ft_load("notexists")

    def test_path_is_not_a_file(self):
        with pytest.raises(FileNotFoundError):
            ft_load(Path(__file__).parent)

    def test_invalid_file_type(self):
        with pytest.raises(ValueError):
            ft_load(Path(__file__))
