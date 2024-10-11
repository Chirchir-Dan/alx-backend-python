#!/usr/bin/env python3
"""
Module for type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and and int OR float v as arguments and
    returns a tuple.
    """
    return (k, float(v ** 2))
