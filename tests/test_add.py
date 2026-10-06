import sys
from pathlib import Path

# Add project root to sys.path (assuming tests/test_add.py)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.add import add, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2