#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a mixed list of ints and floats and returns a float"""
    final: float = 0.0
    for elem in mxd_lst:
        final += elem

    return final
