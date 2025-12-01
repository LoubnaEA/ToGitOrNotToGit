# artifacts/euphues.py

"""Flawed reasoning meets moral test"""

import random

def generate():
    """Return the moral failure or survival"""
    outcomes = [
        "💀 Morality test failed",
        "🌿 Reason prevails (rare)"
    ]
    return [random.choice(outcomes)]
