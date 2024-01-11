#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Method that takes k and v arguments and returns a tuple"""
    return (k, v ** 2)
