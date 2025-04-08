"""
Password generation functionality for the passgen library.
"""

import random
import string
from typing import Optional


def generate(
    length: int = 12,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = True
) -> str:
    """
    Generate a random password with configurable character sets.
    
    Args:
        length (int, optional): The length of the password to generate. 
            Must be between 4 and 64. Defaults to 12.
        uppercase (bool, optional): Include uppercase letters. Defaults to True.
        lowercase (bool, optional): Include lowercase letters. Defaults to True.
        digits (bool, optional): Include digits. Defaults to True.
        symbols (bool, optional): Include symbols. Defaults to True.
    
    Returns:
        str: The generated password.
    
    Raises:
        ValueError: If length is less than 4 or greater than 64.
        ValueError: If no character sets are selected.
    """
    # Validate password length
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    if length > 64:
        raise ValueError("Password length cannot exceed 64 characters")
    
    # Build character set based on configuration
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    
    # Ensure at least one character set is selected
    if not chars:
        raise ValueError("At least one character set must be selected")
    
    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password 