#!/usr/bin/env python3
"""
Module for type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a specified multiplier."""
    def multiplier_function(n: float) -> float:
        """Multiplies n by the specified multiplier"""
        return n * multiplier
    return multiplier_function
