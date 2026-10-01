import unittest

from textutils import character_count, reverse, word_count


class TransformTests(unittest.TestCase):
	def test_counts_whitespace_separated_words(self):
		self.assertEqual(word_count("  hello\nopen source  "), 3)

	def test_counts_all_characters_including_whitespace(self):
		self.assertEqual(character_count("a b\n"), 4)

	def test_reverses_text(self):
		self.assertEqual(reverse("text"), "txet")

	def test_empty_text(self):
		self.assertEqual(word_count(""), 0)
		self.assertEqual(character_count(""), 0)
		self.assertEqual(reverse(""), "")


if __name__ == "__main__":
	unittest.main()
