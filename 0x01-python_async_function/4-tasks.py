#!/usr/bin/env python3
"""
This module provides an asynchronous function to gather
multiple random delays using tasks.
"""

import asyncio
from typing import List

# Import task_wait_random from the module with leading digit
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n random delays between 0 and max_delay seconds using tasks.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A sorted list of the actual delays waited.
    """
    delays = []  # List to store the delays

    # Create a list of tasks to run concurrently using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Await the completion of all tasks
    for task in asyncio.as_completed(tasks):
        delay = await task  # Await each task
        delays.append(delay)  # Append each completed delay to the list

    return sorted(delays)  # Return the sorted list of delays
