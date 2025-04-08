# passgen - Secure & Configurable Password Generator

A pure Python library for generating secure, customizable passwords.

## Features

- Generate passwords with configurable length and character sets
- Include/exclude specific character categories (uppercase, lowercase, digits, symbols)
- Optionally exclude ambiguous characters
- Generate pronounceable passwords
- Estimate password strength

## Installation

```bash
pip install passgen
```

## Quick Start

```python
import passgen

# Generate a random password with default settings (length=12)
password = passgen.generate()
print(password)

# Generate a longer password with specific requirements
password = passgen.generate(
    length=16,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True,
    exclude_ambiguous=True
)
print(password)

# Generate a pronounceable password
pronounceable_password = passgen.generate_pronounceable(length=12)
print(pronounceable_password)

# Check password strength
strength = passgen.check_strength(password)
print(f"Password strength: {strength}")  # Weak, Medium, or Strong
```

## Development

This project uses Test-Driven Development (TDD).

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=passgen
```

## License

MIT 