"""
Pronounceable password generation functionality.
"""

import random
import string
from typing import List, Optional

# Common consonants and vowels for English language
CONSONANTS = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiouy"

# Common syllable patterns
# C = consonant, V = vowel
SYLLABLE_PATTERNS = ["CV", "CVC", "VC", "CVV", "VCC"]

# Common English syllables for more natural-sounding passwords
COMMON_SYLLABLES = [
    "an", "ar", "at", "ca", "co", "de", "di", "ed", "en", "er", "es", "et",
    "in", "is", "it", "la", "le", "ma", "me", "mi", "mo", "na", "ne", "no",
    "on", "or", "pe", "ra", "re", "ri", "ro", "se", "sh", "si", "so", "st",
    "ta", "te", "th", "ti", "to", "tr", "un", "ve", "vi", "wa", "wi"
]


def _generate_syllable() -> str:
    """
    Generate a random pronounceable syllable.
    
    Returns:
        str: A pronounceable syllable.
    """
    # 70% of the time use a common syllable, 30% generate a new one
    if random.random() < 0.7:
        return random.choice(COMMON_SYLLABLES)
    
    # Generate a syllable based on patterns
    pattern = random.choice(SYLLABLE_PATTERNS)
    syllable = ""
    
    for char_type in pattern:
        if char_type == "C":
            syllable += random.choice(CONSONANTS)
        elif char_type == "V":
            syllable += random.choice(VOWELS)
    
    return syllable


def _add_digit(password: str) -> str:
    """
    Add a random digit to the password, preserving the overall length.
    
    Args:
        password (str): The password to modify.
    
    Returns:
        str: The password with a digit added.
    """
    if not password:
        return password
    
    # Choose a random position
    pos = random.randint(0, len(password) - 1)
    
    # Replace the character at that position with a digit
    chars = list(password)
    chars[pos] = random.choice(string.digits)
    
    return ''.join(chars)


def _add_symbol(password: str) -> str:
    """
    Add a random symbol to the password, preserving the overall length.
    
    Args:
        password (str): The password to modify.
    
    Returns:
        str: The password with a symbol added.
    """
    if not password:
        return password
    
    # Choose a random position
    pos = random.randint(0, len(password) - 1)
    
    # Replace the character at that position with a symbol
    chars = list(password)
    chars[pos] = random.choice("!@#$%^&*()-_=+[]{}|;:,.<>/?")
    
    return ''.join(chars)


def _capitalize(password: str) -> str:
    """
    Capitalize some characters in the password.
    
    Args:
        password (str): The password to modify.
    
    Returns:
        str: The password with some characters capitalized.
    """
    if not password:
        return password
    
    # Capitalize around 30% of the letters (but at least 1)
    chars = list(password)
    letter_positions = [i for i, c in enumerate(chars) if c.isalpha()]
    
    if not letter_positions:
        return password
    
    # Determine how many characters to capitalize
    num_to_capitalize = max(1, int(len(letter_positions) * 0.3))
    positions_to_capitalize = random.sample(letter_positions, num_to_capitalize)
    
    for pos in positions_to_capitalize:
        chars[pos] = chars[pos].upper()
    
    return ''.join(chars)


def generate_pronounceable(
    length: int = 12,
    include_digits: bool = False,
    include_symbols: bool = False,
    capitalize: bool = False
) -> str:
    """
    Generate a pronounceable password.
    
    Args:
        length (int, optional): The length of the password to generate.
            Must be between 4 and 64. Defaults to 12.
        include_digits (bool, optional): Include digits. Defaults to False.
        include_symbols (bool, optional): Include symbols. Defaults to False.
        capitalize (bool, optional): Capitalize some characters. Defaults to False.
    
    Returns:
        str: The generated pronounceable password.
    
    Raises:
        ValueError: If length is less than 4 or greater than 64.
    """
    # Validate password length
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    if length > 64:
        raise ValueError("Password length cannot exceed 64 characters")
    
    # Generate syllables until we have enough characters
    password = ""
    while len(password) < length:
        password += _generate_syllable()
    
    # Trim to exact length
    password = password[:length]
    
    # Add digit(s) if requested
    if include_digits:
        # Add 1-3 digits depending on password length
        num_digits = min(max(1, length // 8), 3)
        for _ in range(num_digits):
            password = _add_digit(password)
    
    # Add symbol(s) if requested
    if include_symbols:
        # Add 1-2 symbols depending on password length
        num_symbols = min(max(1, length // 12), 2)
        for _ in range(num_symbols):
            password = _add_symbol(password)
    
    # Capitalize if requested
    if capitalize:
        password = _capitalize(password)
    
    return password 