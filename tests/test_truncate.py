import pytest

from textutils import truncate


def test_truncate():
    assert truncate("Hello World", 20) == "Hello World"
    assert truncate("Hello World", 8) == "Hello..."
    assert truncate("Hello World", 8, suffix="!") == "Hello W!"
    assert truncate("", 5) == ""


def test_truncate_edge_cases():
    assert truncate("Hello", 5) == "Hello"
    assert truncate("Hello", 3, suffix="!") == "He!"
    assert truncate("Hello", 2, suffix="") == "He"
    assert truncate("Hello", 3, suffix="...") == "..."


def test_truncate_rejects_non_string_text():
    with pytest.raises(TypeError):
        truncate(42, 5)


def test_truncate_rejects_max_length_smaller_than_suffix():
    with pytest.raises(ValueError):
        truncate("Hello", 2)
