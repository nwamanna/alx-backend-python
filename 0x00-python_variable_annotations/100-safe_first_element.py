#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ takes in a sequence returns any or none"""
    if lst:
        return lst[0]
    else:
        return None
