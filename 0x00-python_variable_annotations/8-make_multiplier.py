#!/usr/bin/env python3
""" Write a type-annotated function make_multiplier that takes a
    float multiplier as argument and returns a function that multiplies
    a float by multiplier.
"""
from typing import List, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns functions of floats"""
    def multiplyX(x: float) -> float:
        return x * multiplier
    return multiplyX
