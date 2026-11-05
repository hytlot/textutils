"""textutils - une petite librairie de manipulation de texte"""

from textutils.casing import capitalize_words
from textutils.transform import character_count, reverse, word_count
from textutils.truncation import truncate

__all__ = [
    "capitalize_words",
    "character_count",
    "reverse",
    "truncate",
    "word_count",
]
