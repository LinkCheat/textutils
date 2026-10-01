def word_count(text):
	"""Count the whitespace-separated words in text.

	Args:
		text: The text to count words in.

	Returns:
		The number of words in text.
	"""
	return len(text.split())


def character_count(text):
	"""Count all characters in text, including whitespace.

	Args:
		text: The text to count characters in.

	Returns:
		The number of characters in text.
	"""
	return len(text)


def reverse(text):
	"""Return text with its characters in reverse order.

	Args:
		text: The text to reverse.

	Returns:
		A copy of text with its characters reversed.
	"""
	return text[::-1]
