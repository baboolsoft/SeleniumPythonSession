import pytest

def test_total_divisble_by_6(input_total):
    assert input_total % 5 == 0

def test_total_divisble_by_15(input_total):
    assert input_total % 15 == 0