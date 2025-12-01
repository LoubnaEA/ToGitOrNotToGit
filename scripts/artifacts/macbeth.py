# artifacts/macbeth.py

"""Corruption through ambition"""

import random

def generate():
    """Return Macbeth’s moral outcome."""
    outcomes = [
        "💀 Failed morality QA",
        "💀 Ambition overrides human judgment",
        "💀 Prophecies misunderstood; downfall ensured"
    ]
    return [random.choice(outcomes)]
