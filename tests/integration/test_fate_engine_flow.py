# tests/integration/test_fate_engine_flow.py

import pytest
from scripts.fate_engine.prophecy_generator import generate_prophecy

def test_full_flow_integration():
    """Simulate a simple flow using the Fate Engine"""
    characters = ["Hamlet", "Macbeth", "Juliet"]
    prophecies = [generate_prophecy(c) for c in characters]

    for c, p in zip(characters, prophecies):    # Check that all prophecies contain character names
        assert c in p

    assert len(prophecies) == len(characters)   # Ensure we have the same nber of outputs as inputs
