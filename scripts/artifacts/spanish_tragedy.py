# artifacts/spanish_tragedy.py

"""Escalation of revenge"""

import random

def generate():
    """Return a single escalation level outcome"""
    level = random.randint(1, 7)
    if level >= 5:
        return [f"💀 Escalation detected (max level {level})"]
    return [f"🩸 Minor escalation (level {level})"]
