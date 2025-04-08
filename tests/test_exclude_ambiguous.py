"""
Tests for excluding ambiguous characters in password generation.
"""

import pytest
from passgen import generate


def test_exclude_ambiguous_characters():
    """Test that ambiguous characters are excluded when exclude_ambiguous is True."""
    # Define ambiguous characters
    ambiguous_chars = "0O1lI|`'\",;:~-_=+()[]{}<>"
    
    # Generate a password with exclude_ambiguous=True
    password = generate(length=64, exclude_ambiguous=True)
    
    # Check that no ambiguous characters are in the password
    for char in ambiguous_chars:
        assert char not in password, f"Ambiguous character '{char}' found in password"


def test_include_ambiguous_characters():
    """Test that ambiguous characters may be included when exclude_ambiguous is False."""
    # Define ambiguous characters
    ambiguous_chars = "0O1lI|`'\",;:~-_=+()[]{}<>"
    
    # Generate multiple passwords to increase likelihood of including ambiguous characters
    found_ambiguous = False
    for _ in range(20):
        password = generate(length=50, exclude_ambiguous=False)
        if any(c in password for c in ambiguous_chars):
            found_ambiguous = True
            break
    
    assert found_ambiguous, "Failed to generate password with ambiguous characters after multiple attempts"


def test_exclude_ambiguous_default():
    """Test that exclude_ambiguous is False by default."""
    # Define ambiguous characters
    ambiguous_chars = "0O1lI|`'\",;:~-_=+()[]{}<>"
    
    # Generate multiple passwords to increase likelihood of including ambiguous characters
    found_ambiguous = False
    for _ in range(20):
        password = generate(length=50)  # No exclude_ambiguous parameter
        if any(c in password for c in ambiguous_chars):
            found_ambiguous = True
            break
    
    assert found_ambiguous, "Failed to generate password with ambiguous characters after multiple attempts"


def test_exclude_ambiguous_with_character_sets():
    """Test excluding ambiguous characters with specific character sets."""
    # Define ambiguous characters by category
    ambiguous_uppercase = "OI"
    ambiguous_lowercase = "l"
    ambiguous_digits = "01"
    ambiguous_symbols = "|`'\",;:~-_=+()[]{}<>"
    
    # Test with only uppercase
    password = generate(
        length=64,
        uppercase=True,
        lowercase=False,
        digits=False,
        symbols=False,
        exclude_ambiguous=True
    )
    for char in ambiguous_uppercase:
        assert char not in password, f"Ambiguous uppercase '{char}' found in password"
    
    # Test with only lowercase
    password = generate(
        length=64,
        uppercase=False,
        lowercase=True,
        digits=False,
        symbols=False,
        exclude_ambiguous=True
    )
    assert ambiguous_lowercase not in password, f"Ambiguous lowercase '{ambiguous_lowercase}' found in password"
    
    # Test with only digits
    password = generate(
        length=64,
        uppercase=False,
        lowercase=False,
        digits=True,
        symbols=False,
        exclude_ambiguous=True
    )
    for char in ambiguous_digits:
        assert char not in password, f"Ambiguous digit '{char}' found in password"
    
    # Test with only symbols
    password = generate(
        length=64,
        uppercase=False,
        lowercase=False,
        digits=False,
        symbols=True,
        exclude_ambiguous=True
    )
    for char in ambiguous_symbols:
        assert char not in password, f"Ambiguous symbol '{char}' found in password" 