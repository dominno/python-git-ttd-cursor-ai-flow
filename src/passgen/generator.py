"""
Password generation functionality for the passgen library.
"""

import random
import string
from typing import Optional


def generate(length: int = 12) -> str:
    """
    Generate a random password with the specified length.
    
    Args:
        length (int, optional): The length of the password to generate. 
            Must be between 4 and 64. Defaults to 12.
    
    Returns:
        str: The generated password.
    
    Raises:
        ValueError: If length is less than 4 or greater than 64.
    """
    # Validate password length
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    if length > 64:
        raise ValueError("Password length cannot exceed 64 characters")
    
    # Default character set (all printable ASCII except whitespace)
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password 