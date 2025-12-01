# artifacts/hamlet.py

"""Unavoidable tragedy narrative"""

import random

def generate():
    """Return the Hamlet fate as a list of narrative lines"""
    outcomes = [
        "💀 The hesitation seals Hamlet’s fate",
        "💀 No escape from tragic consequence",
        "💀 Ctrl+Z can’t undo destiny"
    ]
    return [random.choice(outcomes)]
