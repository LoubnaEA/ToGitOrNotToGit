# artifacts/random_fate.py

"""Pure unpredictability"""

import random

def generate():
    """Return a single random fate outcome"""
    outcomes = [
        "💀 Fatal outcome",
        "🌿 Survives this act"
    ]
    return [random.choice(outcomes)]
