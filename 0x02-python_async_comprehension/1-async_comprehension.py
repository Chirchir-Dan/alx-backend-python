#!/usr/bin/env python3
"""
This module defines a coroutine that collects random numbers
generated by an asynchronous generator.
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using
    asynchronous comprehension over async_generator.

    The coroutine asynchronously collects and returns
    10 random numbers generated by async_generator.

    Returns:
    --------
    List[float]:
        A list of 10 random floating-point numbers between
        0 and 10.
    """
    return [num async for num in async_generator()]
