# src/mycalc/add.py
from typing import Union

Number = Union[int, float]

def add_numbers(a: Number, b: Number) -> Number:
    return a + b

    # """
    # 嚴格限定數字型別；若傳入非數字（例如字串）則丟出 TypeError。
    # """
    # if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    #     raise TypeError("a and b must be numbers (int or float)")
    # return a + b
