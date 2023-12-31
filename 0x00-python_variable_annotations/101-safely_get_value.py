#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Union, Mapping, Any, TypeVar, Optional
T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """ takes a dictionary returms any or Typevar T"""
    if key in dct:
        return dct[key]
    else:
        return default
