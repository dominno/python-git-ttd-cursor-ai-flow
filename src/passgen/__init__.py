"""
passgen - Secure & Configurable Password Generator

A pure Python library for generating secure, customizable passwords.
"""

from .generator import generate
from .pronounceable import generate_pronounceable
from .strength import calculate_entropy, check_strength

__version__ = "0.1.0" 