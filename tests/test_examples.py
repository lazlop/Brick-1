"""
Tests all example files. See tests/conftest.py for the fixture that generates each of the individual test cases
"""
import brickschema
import pytest


def test_example_file_with_reasoning(filename):
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.load_file(filename)
    g.expand("brick", backend="owlrl")

    valid, _, report = g.validate()
    assert valid, report
