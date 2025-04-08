"""
Tests for pronounceable password generation.
"""

import re
import pytest
from passgen import generate_pronounceable


def test_generate_pronounceable_default():
    """Test generating a pronounceable password with default parameters."""
    password = generate_pronounceable()
    assert password is not None
    assert isinstance(password, str)
    assert len(password) == 12  # Default length should be 12


def test_generate_pronounceable_with_length():
    """Test generating a pronounceable password with a specified length."""
    length = 16
    password = generate_pronounceable(length=length)
    assert len(password) == length

    # Test with minimum length
    min_length = 6  # Pronounceable passwords might need a higher minimum
    password = generate_pronounceable(length=min_length)
    assert len(password) == min_length

    # Test with maximum length
    max_length = 32  # More reasonable max for pronounceable passwords
    password = generate_pronounceable(length=max_length)
    assert len(password) == max_length


def test_pronounceable_password_structure():
    """Test that pronounceable passwords have a valid syllable structure."""
    # Generate a longer password to test pattern
    password = generate_pronounceable(length=24)
    
    # Basic check: alternating consonants and vowels is a common pattern
    # for pronounceable passwords, but not the only possibility
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiouy"
    
    # Ensure there's a reasonable distribution of vowels
    # A pronounceable word usually has at least 1 vowel per 4 chars
    vowel_count = sum(1 for c in password.lower() if c in vowels)
    assert vowel_count >= len(password) // 4, f"Not enough vowels in password: {password}"


def test_invalid_length():
    """Test that invalid length values raise appropriate exceptions."""
    # Test with length too short
    with pytest.raises(ValueError):
        generate_pronounceable(length=3)

    # Test with length too long
    with pytest.raises(ValueError):
        generate_pronounceable(length=65)

    # Test with negative length
    with pytest.raises(ValueError):
        generate_pronounceable(length=-1)


def test_password_randomness():
    """Test that generated pronounceable passwords are random."""
    # Generate multiple passwords and ensure they're different
    passwords = [generate_pronounceable() for _ in range(10)]
    
    # Check that all passwords are unique
    assert len(set(passwords)) == len(passwords), "Pronounceable passwords are not unique"


def test_with_numbers():
    """Test generating pronounceable passwords with numbers."""
    password = generate_pronounceable(length=16, include_digits=True)
    
    # Check that the password contains at least one digit
    assert any(c.isdigit() for c in password), f"No digits in password: {password}"


def test_with_symbols():
    """Test generating pronounceable passwords with symbols."""
    password = generate_pronounceable(length=16, include_symbols=True)
    
    # Check that the password contains at least one symbol
    assert any(not c.isalnum() for c in password), f"No symbols in password: {password}"


def test_with_capitalization():
    """Test generating pronounceable passwords with capital letters."""
    password = generate_pronounceable(length=16, capitalize=True)
    
    # Check that the password contains at least one uppercase letter
    assert any(c.isupper() for c in password), f"No uppercase letters in password: {password}"


def test_all_lowercase():
    """Test generating pronounceable passwords with all lowercase letters."""
    password = generate_pronounceable(length=16, capitalize=False)
    
    # Check that the password contains only lowercase letters
    assert password.islower(), f"Password has uppercase letters: {password}" 