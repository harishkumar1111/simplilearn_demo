import pytest
from app import greet

def test_greet_with_name():
    assert greet("Harish") == "Hello, Harish!"

def test_greet_with_empty_string():
    assert greet("") == "Hello, !"

def test_greet_with_special_characters():
    assert greet("@123") == "Hello, @123!"

def test_greet_with_numbers():
    assert greet("1234") == "Hello, 1234!"
