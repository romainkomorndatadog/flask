print(f"I AM BEING IMPORTED {__file__=}")


# this comment is line 2 and if you didn't know that it'd be easy to miscount below
from my_decorators import outer_decorator, inner_decorator
from unittest.mock import patch

def local_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def test_one_decorator():  # line 11
    str1 = "string 1"
    str2 = "string 2"
    assert str1 != str2

@local_decorator  # line 16
def test_local_decorated():
    str1 = "string 1"
    str2 = "string 2"
    assert str1 == str2

@patch("ddtrace.config._potato", "potato")  # line 22
def test_patched_undecorated():
    str1 = "string 1"
    str2 = "string 2"
    assert str1 != str2

@patch("ddtrace.config._potato", "potato")  # line 28
@inner_decorator
def test_patched_single_decorated():
    str1 = "string 1"
    str2 = "string 2"
    assert str1 == str2

@patch("ddtrace.config._potato", "potato")  # line 35
@outer_decorator
def test_patched_double_decorated():
    str1 = "string 1"
    str2 = "string 2"
    assert str1 != str2

@outer_decorator  # line 42
@patch("ddtrace.config._potato", "potato")
@local_decorator
def test_grand_slam():
    str1 = "string 1"
    str2 = "string 2"
    assert str1 == str2
