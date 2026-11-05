def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Shorten a text to at most ``max_length`` characters.

    The suffix is included in the maximum length.

    Parameters
    ----------
    text : str
        Input text.
    max_length : int
        Maximum length of the returned text, suffix included.
    suffix : str, default="..."
        Text appended when the input is truncated.

    Returns
    -------
    str
        The original text if it fits, otherwise a shortened text ending
        with ``suffix``.

    Raises
    ------
    TypeError
        If text is not a string.
    ValueError
        If max_length is smaller than the length of suffix.

    Examples
    --------
    >>> truncate("Hello World", 8)
    'Hello...'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length < len(suffix):
        raise ValueError("max_length must be at least the length of suffix")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix
