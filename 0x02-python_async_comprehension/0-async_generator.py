#!/usr/bin/env python3
"""
This module defines a coroutine that generates random numbers
between 0 and 10 asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously yields random numbers between
    0 and 10.

    The coroutine loops 10 times, waiting 1 second before
    yielding each random number.

    Yields:
    -------
    float:
        A random number between 0 and 10 after waiting 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
