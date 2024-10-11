#!/usr/bin/env python3
"""
Module for type-annotated fucntion sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument and returns
     their sum as float
    """
    return sum(input_list)
