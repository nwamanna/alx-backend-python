#!/usr/bin/env python3
""" Annotate the below function’s parameters and return values
    with the appropriate types
"""
from typing import List, Sequence, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """ return a tuple"""
    return [(i, len(i)) for i in lst]
