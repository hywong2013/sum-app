# tests/unit/test_add.py
import math
import pytest
from mycalc.add import add_numbers

def test_add_integers():
    assert add_numbers(2, 3) == 5

def test_add_floats():
    assert math.isclose(add_numbers(3.2, 0.3), 3.5, rel_tol=1e-12)

def test_add_negatives():
    assert add_numbers(-10, -5) == -15

def test_add_mixed_sign():
    assert add_numbers(-2, 5) == 3

def test_add_large_numbers():
    a = 10**18
    b = 10**18
    assert add_numbers(a, b) == 2 * 10**18

def test_reject_string_inputs():
    with pytest.raises(TypeError):
        add_numbers("2", "3")  # 應拒絕非數字型別
