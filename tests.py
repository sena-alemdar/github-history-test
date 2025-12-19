"""Tests for app.py"""

from app import greet, add

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
