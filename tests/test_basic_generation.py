import pytest
from passgen import generate


def test_generate_default_password():
    """Test generating a password with default parameters."""
    password = generate()
    assert password is not None
    assert isinstance(password, str)
    assert len(password) == 12  # Default length should be 12


def test_generate_password_with_length():
    """Test generating a password with a specified length."""
    length = 16
    password = generate(length=length)
    assert len(password) == length

    # Test with minimum length
    min_length = 4
    password = generate(length=min_length)
    assert len(password) == min_length

    # Test with maximum length
    max_length = 64
    password = generate(length=max_length)
    assert len(password) == max_length


def test_invalid_length():
    """Test that invalid length values raise appropriate exceptions."""
    # Test with length too short
    with pytest.raises(ValueError):
        generate(length=3)

    # Test with length too long
    with pytest.raises(ValueError):
        generate(length=65)

    # Test with negative length
    with pytest.raises(ValueError):
        generate(length=-1)


def test_password_randomness():
    """Test that generated passwords are random."""
    # Generate multiple passwords and ensure they're different
    passwords = [generate() for _ in range(10)]
    
    # Check that all passwords are unique
    assert len(set(passwords)) == len(passwords) 