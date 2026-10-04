# TextUtils

TextUtils is a simple Python library that provides useful text manipulation functions.

## Features

- **Word count:** Count the number of words in a text.
- **Character count:** Count the number of characters in a text.
- **Reverse text:** Reverse the characters in a string.
- **Capitalize words:** Capitalize the first letter of each word.
- **Truncate text:** Shorten text to a maximum length, including a configurable suffix.

## Project structure

```text
textutils/
├── textutils/
│   ├── __init__.py
│   ├── casing.py
│   ├── transform.py
│   └── truncate.py
├── tests/
│   ├── test_casing.py
│   ├── test_transform.py
│   └── test_truncate.py
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/hytlot/textutils.git
cd textutils
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

## Usage

```python
from textutils.transform import word_count, character_count, reverse
from textutils.casing import capitalize_words
from textutils import truncate

text = "hello open source"

print(word_count(text))         # 3
print(character_count(text))    # 18
print(reverse(text))            # ecruos nepo olleh
print(capitalize_words(text))   # Hello Open Source
print(truncate("Hello World", 8))  # Hello...
```

## Running tests

Install pytest:

```bash
python -m pip install pytest
```

Run the tests:

```bash
python -m pytest
```

## License

This project is distributed under the MIT License. See the `LICENSE` file for details.