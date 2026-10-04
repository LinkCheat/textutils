# textutils
A lightweight Python library for common text-processing operations.
## Features
- `word_count(text)` counts whitespace-separated words.
- `character_count(text)` counts every character, including whitespace.
- `reverse(text)` returns the text in reverse order.
- `capitalize_words(text)` capitalizes each word.
- `count_vowels(text)` counts uppercase and lowercase English vowels (A, E, I, O, U).
## Installation
python -m pip install .
## Usage
```python
from textutils import (
	capitalize_words,
	character_count,
	count_vowels,
	reverse,
	word_count,
)

text = "hello open source"
print(word_count(text))         # 3
print(character_count(text))    # 17
print(reverse(text))            # ecruos nepo olleh
print(capitalize_words(text))   # Hello Open Source
print(count_vowels("Hello, world!"))  # 3
```
## Contributing
Contributions are welcome!
## License
MIT License