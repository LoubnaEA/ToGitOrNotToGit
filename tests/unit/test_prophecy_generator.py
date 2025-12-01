# tests/unit/test_prophecy_generator.py

import pytest
from scripts.fate_engine.prophecy_generator import generate_prophecy

def test_generate_prophecy_returns_string():
    """Check that generate_prophecy returns a string"""
    result = generate_prophecy("Hamlet")
    assert isinstance(result, str)

def test_generate_prophecy_includes_character():
    """Check that character name appears in the prophecy"""
    character = "Ophelia"
    result = generate_prophecy(character)
    assert character in result

def test_generate_prophecy_randomness():
    """Check that multiple calls produce varied outputs"""
    results = {generate_prophecy("Hamlet") for _ in range(10)}
    assert len(results) > 1     # there should be some variation
