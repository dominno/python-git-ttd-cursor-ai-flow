"""
Tests for password strength estimation.
"""

import pytest
from passgen import check_strength, calculate_entropy


def test_entropy_calculation():
    """Test that entropy calculation works correctly."""
    # Empty password has 0 entropy
    assert calculate_entropy("") == 0
    
    # A single character from a small pool has low entropy
    assert calculate_entropy("a") == pytest.approx(4.7, 0.1)  # log2(26)
    
    # A longer password has higher entropy
    assert calculate_entropy("password") == pytest.approx(37.6, 0.1)  # 8 * log2(26)
    
    # Mixed case increases entropy
    assert calculate_entropy("Password") > calculate_entropy("password")
    
    # Adding digits increases entropy
    assert calculate_entropy("password123") > calculate_entropy("password")
    
    # Adding symbols increases entropy
    assert calculate_entropy("password!@#") > calculate_entropy("password")
    
    # Random string from all character types has highest entropy
    assert calculate_entropy("aB3$xY7*") > calculate_entropy("password123")


def test_entropy_with_character_sets():
    """Test entropy calculation with different character sets."""
    # Only lowercase (pool size 26)
    assert calculate_entropy("abcdefgh") == pytest.approx(8 * 4.7, 0.1)  # 8 * log2(26)
    
    # Only uppercase (pool size 26)
    assert calculate_entropy("ABCDEFGH") == pytest.approx(8 * 4.7, 0.1)  # 8 * log2(26)
    
    # Only digits (pool size 10)
    assert calculate_entropy("12345678") == pytest.approx(8 * 3.32, 0.1)  # 8 * log2(10)
    
    # Lowercase + uppercase (pool size 52)
    assert calculate_entropy("abCDEfgh") == pytest.approx(8 * 5.7, 0.1)  # 8 * log2(52)
    
    # Lowercase + digits (pool size 36)
    assert calculate_entropy("abcd1234") == pytest.approx(8 * 5.17, 0.1)  # 8 * log2(36)
    
    # All character types (pool size ~94)
    assert calculate_entropy("aB3$xY7*") == pytest.approx(8 * 6.55, 0.1)  # 8 * log2(94)


def test_check_strength_weak():
    """Test that weak passwords are correctly identified."""
    # Short passwords
    assert check_strength("abc") == "Weak"
    assert check_strength("123456") == "Weak"
    
    # Common patterns
    assert check_strength("password") == "Weak"
    assert check_strength("qwerty") == "Weak"
    assert check_strength("12345678") == "Weak"
    
    # Single character set
    assert check_strength("abcdefghijklm") == "Weak"  # Even if long, using only lowercase is weak


def test_check_strength_medium():
    """Test that medium-strength passwords are correctly identified."""
    # Mixed case but still fairly short
    assert check_strength("Password1") == "Medium"
    
    # Longer but with limited character sets
    assert check_strength("passwordpassword") == "Medium"
    
    # Mixed case and digits but no symbols
    assert check_strength("Password123") == "Medium"
    
    # Mixed case and symbols but short
    assert check_strength("Pass!@#") == "Medium"


def test_check_strength_strong():
    """Test that strong passwords are correctly identified."""
    # Long with mixed case, digits, and symbols
    assert check_strength("P@ssw0rd!2023XyZ") == "Strong"
    
    # Random string with all character types
    assert check_strength("aB3$xY7*cD9!eF") == "Strong"
    
    # Long pronounceable with mixed case, digits, and symbols
    assert check_strength("Correct-Horse-Battery-Staple-99!") == "Strong"
    
    # Shorter but high entropy due to all character types
    assert check_strength("P@s$w0rD!") == "Strong"


def test_check_strength_edge_cases():
    """Test edge cases for strength checking."""
    # Empty password
    assert check_strength("") == "Weak"
    
    # Very short password
    assert check_strength("a") == "Weak"
    
    # Very long password (should be strong even with just lowercase)
    assert check_strength("a" * 64) == "Strong"
    
    # Password with spaces
    assert check_strength("this is a password") == "Medium"
    
    # Password with unicode characters
    assert check_strength("パスワード123") == "Medium"  # Japanese for "password" 