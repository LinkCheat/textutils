import unittest

from textutils import capitalize_words


class CapitalizeWordsTests(unittest.TestCase):
	def test_capitalizes_each_word(self):
		self.assertEqual(capitalize_words("hello open source"), "Hello Open Source")

	def test_preserves_whitespace(self):
		self.assertEqual(capitalize_words("hello\nworld"), "Hello\nWorld")


if __name__ == "__main__":
	unittest.main()
