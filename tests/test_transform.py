
from textutils.transform import word_count, character_count, reverse


def test_word_count():
    assert word_count("Hello Open Source") == 3
    assert word_count("") == 0
    assert word_count("Python") == 1
    assert word_count("Hello   World") == 2


def test_character_count():
    assert character_count("Hello") == 5
    assert character_count("") == 0
    assert character_count("Hello World") == 11


def test_reverse():
    assert reverse("Python") == "nohtyP"
    assert reverse("") == ""
    assert reverse("Hello World") == "dlroW olleH"
