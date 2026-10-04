import unittest

from textutils import count_vowels


class VowelCounterTests(unittest.TestCase):
	def test_counts_uppercase_and_lowercase_vowels(self):
		self.assertEqual(count_vowels("Hello, world!"), 3)
		self.assertEqual(count_vowels("AEIOU aeiou"), 10)

	def test_ignores_non_vowels(self):
		self.assertEqual(count_vowels("rhythm 123!?"), 0)

	def test_empty_text(self):
		self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
	unittest.main()
