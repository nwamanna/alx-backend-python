#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, str]]) -> float:
    """ returns sum of the elements of floats from the function"""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
