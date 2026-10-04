def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Shorten text to at most max_length characters, including the suffix.

    Args:
        text: The input text.
        max_length: The maximum length of the returned text.
        suffix: The text to append when the input is truncated.

    Returns:
        The original text when it fits, otherwise a shortened text with suffix.

    Raises:
        TypeError: If text is not a string.
        ValueError: If max_length is smaller than the suffix length.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length < len(suffix):
        raise ValueError("max_length must be at least the length of suffix")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix
