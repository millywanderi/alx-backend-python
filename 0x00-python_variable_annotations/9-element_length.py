#!/usr/bin/env python3
"""
Module that duck type an iterable object
"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A method that return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
