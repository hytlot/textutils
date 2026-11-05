def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    str
        Text with each word capitalized.

    Examples
    --------
    >>> capitalize_words("hello open source")
    'Hello Open Source'
    """
    return text.title()
