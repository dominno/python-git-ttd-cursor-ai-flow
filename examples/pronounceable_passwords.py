#!/usr/bin/env python3
"""
Example script demonstrating pronounceable password generation.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from passgen import generate_pronounceable

# Generate a basic pronounceable password
basic = generate_pronounceable()
print(f"Basic pronounceable password: {basic}")

# Generate a pronounceable password with numbers
with_numbers = generate_pronounceable(length=16, include_digits=True)
print(f"Pronounceable with numbers: {with_numbers}")

# Generate a pronounceable password with symbols
with_symbols = generate_pronounceable(length=16, include_symbols=True)
print(f"Pronounceable with symbols: {with_symbols}")

# Generate a pronounceable password with capitalization
with_caps = generate_pronounceable(length=16, capitalize=True)
print(f"Pronounceable with capitals: {with_caps}")

# Generate a complete pronounceable password with all options
complete = generate_pronounceable(
    length=20,
    include_digits=True,
    include_symbols=True,
    capitalize=True
)
print(f"Complete pronounceable password: {complete}") 