# src/mycalc/add.py
from typing import Union

Number = Union[int, float]

def validate_number(value) -> Number:
    """
    檢查輸入是否為 int 或 float。
    若不是數字型別，拋出 TypeError。
    """
    # if not isinstance(value, (int, float)):
    #     raise TypeError(f"Value must be int or float, got {type(value).__name__}")
    return value

def add_numbers(a: Number, b: Number) -> Number:
    """
    加總兩個數字，在加總前會先檢查型別。
    """
    a = validate_number(a)
    b = validate_number(b)
    return a + b
