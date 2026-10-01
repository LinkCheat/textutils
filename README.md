# textutils
A lightweight Python library for common text-processing operations.
## Features
- `word_count(text)` counts whitespace-separated words.
- `character_count(text)` counts every character, including whitespace.
- `reverse(text)` returns the text in reverse order.
- `capitalize_words(text)` capitalizes each word.
## Installation
python -m pip install .
## Usage
```python
from textutils import (
	capitalize_words,
	character_count,
	reverse,
	word_count,
)

text = "hello open source"
print(word_count(text))         # 3
print(character_count(text))    # 17
print(reverse(text))            # ecruos nepo olleh
print(capitalize_words(text))   # Hello Open Source
```
## Contributing
Contributions are welcome!
## License
MIT License