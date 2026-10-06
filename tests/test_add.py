import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from src.add import add, sub


# --- Tests for add() ---

def test_add_positive_integers():
    assert add(2, 3) == 6


def test_add_negative_integers():
    assert add(-4, -6) == -10
    assert add(-5, 10) == 5


def test_add_with_zero():
    assert add(0, 7) == 7
    assert add(0, 0) == 0


def test_add_floating_numbers():
    assert pytest.approx(add(1.2, 3.4), rel=1e-5) == 4.6


# --- Tests for sub() ---

def test_sub_positive_integers():
    assert sub(5, 3) == 2


def test_sub_resulting_negative():
    assert sub(3, 5) == -2


def test_sub_negative_integers():
    assert sub(-5, -2) == -3
    assert sub(-5, 2) == -7


def test_sub_with_zero():
    assert sub(9, 0) == 9
    assert sub(0, 4) == -4
    assert sub(0, 0) == 0