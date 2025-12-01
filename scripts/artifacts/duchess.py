# artifacts/duchess.py

"""Secrets under pressure"""

import random

def generate():
    """Return the Duchess’s secret outcome"""
    outcomes = [
        "💀 Secret revealed",
        "🌿 Secret survives"
    ]
    return [random.choice(outcomes)]
