"""
Tests for configurable character sets in password generation.
"""

import string
import pytest
from passgen import generate


def test_uppercase_only():
    """Test generating a password with only uppercase letters."""
    password = generate(length=12, uppercase=True, lowercase=False, digits=False, symbols=False)
    assert password.isupper()
    assert len(password) == 12
    assert all(c in string.ascii_uppercase for c in password)


def test_lowercase_only():
    """Test generating a password with only lowercase letters."""
    password = generate(length=12, uppercase=False, lowercase=True, digits=False, symbols=False)
    assert password.islower()
    assert len(password) == 12
    assert all(c in string.ascii_lowercase for c in password)


def test_digits_only():
    """Test generating a password with only digits."""
    password = generate(length=12, uppercase=False, lowercase=False, digits=True, symbols=False)
    assert password.isdigit()
    assert len(password) == 12
    assert all(c in string.digits for c in password)


def test_symbols_only():
    """Test generating a password with only symbols."""
    password = generate(length=12, uppercase=False, lowercase=False, digits=False, symbols=True)
    assert len(password) == 12
    assert all(c in string.punctuation for c in password)


def test_combined_character_sets():
    """Test generating a password with combined character sets."""
    # Uppercase and lowercase
    password = generate(length=20, uppercase=True, lowercase=True, digits=False, symbols=False)
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert not any(c in string.digits for c in password)
    assert not any(c in string.punctuation for c in password)
    
    # Uppercase and digits
    password = generate(length=20, uppercase=True, lowercase=False, digits=True, symbols=False)
    assert any(c in string.ascii_uppercase for c in password)
    assert not any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert not any(c in string.punctuation for c in password)
    
    # Lowercase and symbols
    password = generate(length=20, uppercase=False, lowercase=True, digits=False, symbols=True)
    assert not any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert not any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)


def test_default_includes_all_character_sets():
    """Test that the default password includes all character sets."""
    # Generate a longer password to ensure all character sets are likely to be included
    password = generate(length=32)
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)


def test_no_character_sets_selected():
    """Test that an error is raised when no character sets are selected."""
    with pytest.raises(ValueError):
        generate(uppercase=False, lowercase=False, digits=False, symbols=False) 