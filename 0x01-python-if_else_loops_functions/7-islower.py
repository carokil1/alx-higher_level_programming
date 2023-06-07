#!/usr/bin/python3
# 7-islower.py

def is_lower(char):
    """Check if a character is lowercase."""
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False
