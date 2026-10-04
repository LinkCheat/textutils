"""Small utilities for common text-processing tasks."""

from .casing import capitalize_words
from .counter import count_vowels
from .transform import character_count, reverse, word_count

__all__ = ["word_count", "character_count", "reverse", "capitalize_words", "count_vowels"]
