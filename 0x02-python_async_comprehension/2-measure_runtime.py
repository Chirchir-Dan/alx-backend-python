#!/usr/bin/env python3
"""
This module defines a coroutine that measures the runtime of
executing async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
    --------
    float:
        The total runtime (in seconds) of running async_comprehension
        four times concurrently.
    """
    start_time = time.perf_counter()  # Start the timer

    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # End the timer
    return end_time - start_time
