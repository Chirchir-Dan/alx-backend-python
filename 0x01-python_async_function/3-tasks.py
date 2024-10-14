#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.
Task for waiting on a random delay.
"""

import asyncio

# Import wait_random from the module with leading digit
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that runs wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The task representing the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
