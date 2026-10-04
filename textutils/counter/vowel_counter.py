def count_vowels(text):
	"""Count the English vowels in text.

	Args:
		text: The text to examine.

	Returns:
		The number of uppercase and lowercase A, E, I, O, and U characters.
	"""
	return sum(character.lower() in "aeiou" for character in text)
