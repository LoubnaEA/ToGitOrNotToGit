# artifacts/ophelia.py

"""Emotional fragmentation"""

import random

def generate():
    """Return Ophelia’s emotional fate"""
    options = {
        "grieving": "💀 Drowned",
        "ignored": "💀 Lost mind",
        "overwhelmed": "🌿 Survives"
    }
    condition = random.choice(list(options.keys()))
    return [f"{condition}: {options[condition]}"]
