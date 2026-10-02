def word_count(text: str) -> int:
    """
    Count the number of words in a text.

    Args:
        text: The input text.

    Returns:
        The number of words.
    """
    return len(text.split())


def character_count(text: str) -> int:
    """
    Count the number of characters in a text, including spaces.

    Args:
        text: The input text.

    Returns:
        The number of characters.
    """
    return len(text)


def reverse(text: str) -> str:
    """
    Reverse the characters of a text.

    Args:
        text: The input text.

    Returns:
        The reversed text.
    """
    return text[::-1]