from textutils.casing import capitalize_words


def test_capitalize_words():
    assert capitalize_words("hello open source") == "Hello Open Source"
    assert capitalize_words("") == ""
    assert capitalize_words("python") == "Python"
    assert capitalize_words("HELLO WORLD") == "Hello World"