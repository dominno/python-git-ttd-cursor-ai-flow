#!/usr/bin/env python3
"""
Example script demonstrating password strength estimation.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from passgen import generate, generate_pronounceable, calculate_entropy, check_strength

# Generate and check a random password
password = generate(length=12)
entropy = calculate_entropy(password)
strength = check_strength(password)
print(f"Random password: {password}")
print(f"Entropy: {entropy:.2f} bits")
print(f"Strength: {strength}")
print()

# Generate and check a configurable password
config_password = generate(
    length=16,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True
)
entropy = calculate_entropy(config_password)
strength = check_strength(config_password)
print(f"Configurable password: {config_password}")
print(f"Entropy: {entropy:.2f} bits")
print(f"Strength: {strength}")
print()

# Generate and check a pronounceable password
pronounceable = generate_pronounceable(
    length=16,
    include_digits=True,
    include_symbols=True,
    capitalize=True
)
entropy = calculate_entropy(pronounceable)
strength = check_strength(pronounceable)
print(f"Pronounceable password: {pronounceable}")
print(f"Entropy: {entropy:.2f} bits")
print(f"Strength: {strength}")
print()

# Check some example passwords
examples = [
    "password",
    "Password123",
    "P@ssw0rd!",
    "correct-horse-battery-staple",
    "1qaz2wsx3edc",
    "abcdefghijklmnopqrstuvwxyz"
]

print("Example Passwords:")
for example in examples:
    entropy = calculate_entropy(example)
    strength = check_strength(example)
    print(f"Password: {example}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Strength: {strength}")
    print() 