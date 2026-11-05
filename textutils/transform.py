def word_count(text: str) -> int:
    """Count the number of words in a text.

    Parameters
    ----------
    text : str
        Input text whose words are counted.

    Returns
    -------
    int
        Number of words in the input text.

    Examples
    --------
    >>> word_count("Hello Open Source")
    3
    """
    return len(text.split())


def character_count(text: str) -> int:
    """Count the number of characters in a text, including spaces.

    Parameters
    ----------
    text : str
        Input text whose characters are counted.

    Returns
    -------
    int
        Number of characters in the input text.

    Examples
    --------
    >>> character_count("Hello World")
    11
    """
    return len(text)


def reverse(text: str) -> str:
    """Reverse the characters of a text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    str
        Text with its characters in reverse order.

    Examples
    --------
    >>> reverse("Python")
    'nohtyP'
    """
    return text[::-1]
