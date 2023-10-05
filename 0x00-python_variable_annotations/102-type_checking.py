#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ takes in  a tuple returns a list"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
