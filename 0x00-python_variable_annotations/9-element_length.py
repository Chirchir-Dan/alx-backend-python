#!/usr/bin/env python3
"""
Module to compute the length of each element in a list.

This module provides the `element_length` function, which takes a list
as input and returns a list of tuples. Each tuple contains an element
from the input list and its corresponding length.
"""
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """Returns a list of tuples containing each element and its length.

    Args:
        lst (List[Any]): A list containing elements of any type.

    Returns:
        List[Tuple[Any, int]]: A list of tuples, where each tuple contains
        an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
